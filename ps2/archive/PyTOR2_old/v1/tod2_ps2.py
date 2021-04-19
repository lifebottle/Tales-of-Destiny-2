import sys
import os
import json
import struct
import subprocess

low_bits = 0x3F
high_bits = 0xFFFFFFC0
pointer_begin = 0xDD320
pointer_end = 0xE62EF
types = {'lzssrle': 3, 'dummy': 99, 'lzss': 1, 'iecs': 4}
ext = {83: 'SCPK', 73: 'IECS'}
compress_decompress = True

def get_pointers():
    f = open("SLPS_251.72", 'rb')
    f.seek(pointer_begin, 0)
    pointers = []

    while f.tell() < pointer_end:
        p = struct.unpack('<L', f.read(4))[0]
        pointers.append(p)

    f.close()
    return pointers

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def compress_comptoe(name, ctype=1):
    if ctype == 1:
        subprocess.run(['comptoe', '-c1', name, name + '.c'])
    else:
        subprocess.run(['comptoe', '-c3', name, name + '.c'])

def decompress_comptoe(name):
    subprocess.run(['comptoe', '-d', name, name + '.c'])

def extract_fpb():
    f = open('FILE.FPB', 'rb')
    mkdir('FPB')
    json_file = open('FPB.json', 'w')
    json_data = {}

    pointers = get_pointers()
    
    for i in range(len(pointers)-1):
        remainder = pointers[i] & low_bits
        start = pointers[i] & high_bits
        end = (pointers[i+1] & high_bits) - remainder
        size = end - start
        if size == 0:
            json_data[i] = types['dummy']
            continue
        f.seek(start, 0)
        data = f.read(size)
        json_data[i] = data[0]
        extension = 'bin'
        if data[0] in ext.keys():
            extension = ext[data[0]]
        o = open('FPB/' + '%04d.%s' % (i, extension), 'wb')
        o.write(data)
        o.close()
        print (i)

    json.dump(json_data, json_file, indent=4)
    f.close()

def pack_fpb():
    sectors = [0]
    remainders = []
    buffer = 0
    json_file = open('fpb.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    o = open('new_file.fpb', 'wb')
    
    for k, v in json_data.items():
        size = 0
        remainder = 0
        if v != types["dummy"]:
            extension = 'bin'
            if v in ext:
                extension = ext[v]
            f = open('fpb/%04d.%s' % (int(k), extension), 'rb')
            o.write(f.read())
            size = os.path.getsize('fpb/%04d.%s' % (int(k), extension))
            remainder = 0x40 - (size % 0x40)
            if remainder == 0x40:
                remainder = 0
            o.write(b'\x00' * remainder)
            f.close()
        remainders.append(remainder)
        buffer += (size + remainder)
        sectors.append(buffer)
        print (k)

    u = open('new_SLPS_251.72', 'r+b')
    u.seek(pointer_begin)
    
    for i in range(len(sectors)-1):
        u.write(struct.pack('<L', sectors[i] + remainders[i]))
        
    o.close()
    u.close()

def extract_scpk():
    mkdir('scpk')
    json_file = open('SCPK.json', 'w')
    json_data = {}
    
    for file in os.listdir('fpb'):
        if not file.endswith('SCPK'):
            continue
        f = open('fpb/%s' % file, 'rb')
        header = f.read(4)
        if header != b'SCPK':
            f.close()
            continue
        mkdir('scpk/%s' % file[:-4])
        index = int(file[:-5])
        json_data[index] = {}
        f.read(4)
        files = struct.unpack('<L', f.read(4))[0]
        f.read(4)
        sizes = []
        for i in range(files):
            sizes.append(struct.unpack('<L', f.read(4))[0])
        for i in range(files):
            o = open('scpk/%s/%02d.bin' % (file[:-5], i), 'wb')
            data = f.read(sizes[i])
            json_data[index][i] = data[0]
            o.write(data)
            o.close()
            if compress_decompress:
                if i == files-1:
                    if data[0] == 1 or data[0] == 3:
                        decompress_comptoe('scpk/%s/%02d.bin' % (file[:-5], i))
                        os.remove('scpk/%s/%02d.bin' % (file[:-5], i))
                        os.rename('scpk/%s/%02d.bin.c' % (file[:-5], i), 'scpk/%s/%02d.bin' % (file[:-5], i))

        f.close()
        print (file)
        
    json.dump(json_data, json_file, indent=4)

def pack_scpk():
    mkdir('scpk_packed')
    json_file = open('scpk.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    for folder in os.listdir('scpk/'):
        if os.path.isdir('scpk/' + folder):
            sizes = []
            o = open('scpk_packed/%s.SCPK' % folder, 'wb')
            data = bytearray()
            listdir = os.listdir('scpk/' + folder)
            for file in listdir:
                read = b''
                index = str(int(file[:-4]))
                f = open('scpk/%s/%s' % (folder, file), 'rb')
                ctype = json_data[folder][index]
                if file == listdir[-1]:
                    if ctype != 0:
                        if compress_decompress:
                            compress_comptoe('scpk/%s/%s' % (folder, file), ctype)
                            comp = open('scpk/%s/%s.c' % (folder, file), 'rb')
                            read = comp.read()
                            comp.close()
                            os.remove('scpk/%s/%s.c' % (folder, file))
                        else:
                            read = f.read()
                    else:
                        read = f.read()
                else:
                    read = f.read()
                data += read
                sizes.append(len(read))
                f.close()
                
            o.write(b'\x53\x43\x50\x4B\x01\x00\x07\x00')
            o.write(struct.pack('<L', len(sizes)))
            o.write(b'\x00' * 4)
            
            for i in range(len(sizes)):
                o.write(struct.pack('<L', sizes[i]))
                
            o.write(data)
            o.close()
            
        print (folder)
        
if __name__ == '__main__':
    if sys.argv[1] == '1':
        extract_fpb()
    elif sys.argv[1] == '2':
        pack_fpb()
    elif sys.argv[1] == '3':
        extract_scpk()
    elif sys.argv[1] == '4':
        pack_scpk()
    else:
        sys.exit(1)

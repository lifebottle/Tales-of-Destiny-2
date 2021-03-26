import sys
import os
import json
import struct
import zlib

types = {'raw': 0, 'compressed': 1, 'dummy' : 2}

pointer_begin = 0x29531C
pointer_end = 0x29E9AC
    
def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass
    
def get_pointers():
    f = open("ULJS00097.bin", 'rb')
    f.seek(pointer_begin, 0)
    pointers = []

    while f.tell() < pointer_end:
        p = struct.unpack('<L', f.read(4))[0]
        pointers.append(p)

    for i in range(len(pointers)-1):
        remainder = pointers[i] & 0x7FF
        start = pointers[i] & 0xFFFFF800
        end = (pointers[i+1] & 0xFFFFF800) - remainder

    f.close()
    return pointers

def decompress(data):
    if data[0] != 4:
        return data
    try:
        decompressed = zlib.decompress(data[0x9:], wbits = -15)
    except:
        return data
    return decompressed

def compress(data):
    compressed = zlib.compress(data, 7)
    header = b'\x04'
    header += struct.pack('<L', len(compressed))
    header += struct.pack('<L', len(data))
    return header + compressed

def decompress_file(name):
    f = open(name, 'rb')
    data = decompress(f.read())
    o = open(name + '.decompressed', 'wb')
    o.write(data)
    f.close()
    o.close()
    print ("Decompressed")

def compress_file(name):
    f = open(name, 'rb')
    data = compress(f.read())
    o = open(name + '.compressed', 'wb')
    o.write(data)
    f.close()
    o.close()
    print ("Compressed")
    
def extract_fpb():
    f = open('FILE.FPB', 'rb')

    mkdir('FPB')

    json_file = open('FPB.json', 'w')
    json_data = {}

    pointers = get_pointers()
    
    for i in range(len(pointers)-1):
        remainder = pointers[i] & 0x7FF
        start = pointers[i] & 0xFFFFF800
        end = (pointers[i+1] & 0xFFFFF800) - remainder

        f.seek(start, 0)
        size = (end - start)
        o = open('FPB/' + '%04d.bin' % i, 'wb')
        data = f.read(size)
        if size == 0:
            json_data[i] = types['dummy']
            continue
        elif data[0] == 4:
            json_data[i] = types['compressed']
            data = decompress(data)
        else:
            json_data[i] = types['raw']
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
        if v == types["dummy"]:
            size = 0
            remainder = 0
        else:
            f = open('fpb/%04d.bin' % int(k), 'rb')
            size = os.path.getsize('fpb/%04d.bin' % int(k))
            remainder = 0x800 - (size % 0x800)
            if remainder == 0x800:
                remainder = 0
            if v == types["raw"]:
                o.write(f.read())
            else:
                o.write(compress(f.read()))
            o.write(b'\x00' * remainder)
            f.close()
        remainders.append(remainder)
        buffer += (size + remainder)
        sectors.append(buffer)
        print (k)

    u = open('new_ULJS00097.bin', 'r+b')
    u.seek(pointer_begin)
    
    for i in range(len(sectors)):
        u.write(struct.pack('<L', sectors[i] + remainders[i]))
        
    o.close()
    u.close()

def extract_scpk():
    mkdir('scpk_')

    json_file = open('SCPK.json', 'w')
    json_data = {}
    
    for file in os.listdir('fpb'):
        f = open('fpb/%s' % file, 'rb')
        header = f.read(4)
        if header != b'SCPK':
            continue
        mkdir('scpk_/%s' % file[:-4])
        index = int(file[:-4])
        json_data[index] = {}
        f.read(4)
        files = struct.unpack('<L', f.read(4))[0]
        f.read(4)
        sizes = []
        for i in range(files):
            sizes.append(struct.unpack('<L', f.read(4))[0])

        for i in range(files):
            o = open('scpk_/%s/%02d.bin' % (file[:-4], i), 'wb')
            data = f.read(sizes[i])
            if data[0] == 4:
                json_data[index][i] = types["compressed"]
            else:
                json_data[index][i] = types["raw"]
            data = decompress(data)
            o.write(data)
            o.close()

        f.close()
        print (file)
        
    json.dump(json_data, json_file, indent=4)

def pack_scpk():
    mkdir('scpk_packed')
    json_file = open('scpk.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    
    for folder in os.listdir('scpk_/'):
        if os.path.isdir('scpk_/' + folder):
            sizes = []
            o = open('scpk_packed/%s.bin' % folder, 'wb')
            data = bytearray()
            for file in os.listdir('scpk_/' + folder):
                f = open('scpk_/%s/%s' % (folder, file), 'rb')
                read = f.read()
                index = folder
                index2 = str(int(file[:-4]))
                if json_data[index][index2] == types["compressed"]:
                    read = compress(read)
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
    #extract_fpb()
    #pack_fpb()
    #decompress_file('0000.bin')
    #compress_file('0000.bin.decompressed')
    #extract_scpk()
    pack_scpk()
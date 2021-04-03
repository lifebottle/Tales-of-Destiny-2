import os, sys, struct, subprocess, json

# True to automatically compress after packing
# False to only pack
compress = True

def extract_pak1():
    print ("Extracting pak1...")
    for name in os.listdir('pak1'):
        if not name.endswith('pak1'):
            continue
        f = open('pak1/' + name, 'rb')
        try: os.mkdir('pak1/' + name[:5])
        except: pass
        n = struct.unpack('<I', f.read(4))[0]
        offsets = []
        sizes = []
        for i in range(n):
            offsets.append(struct.unpack('<I', f.read(4))[0])
            sizes.append(struct.unpack('<I', f.read(4))[0])
        for i in range(n):
            f.seek(offsets[i], 0)
            data = f.read(sizes[i])
            ext = 'bin'
            if len(data) > 4:
                if data[:4] == b'TM2@':
                    ext = 'tm2'
                elif data[:4] == b'SCED':
                    ext = 'sced'
                else:
                    pass
            o = open('pak1/' + name[:5] + '/' + '%s_%02d.%s' % (name[:5], i, ext), 'wb')
            o.write(data)
            o.close()
        f.close()

def insert_pak1():
    json_file = open('compression.json', 'r')
    json_data = json.load(json_file)
    json_file.close()
    print ("Packing pak1...")
    try: os.mkdir('pak1_packed')
    except: pass
    for name in os.listdir('pak1'):
        if not os.path.isdir('pak1/' + name):
            continue
        dir_ = os.listdir('pak1/' + name)
        files = []
        paddings = []
        n = len(dir_)
        for file in dir_:
            f = open('pak1/' + name + '/' + file, 'rb')
            data = f.read()
            padding = 16 - (len(data) % 16)
            if padding == 16:
                padding = 0
            files.append(data)
            paddings.append(padding)
        fname = 'pak1_packed/' + name + '.pak1'
        o = open(fname, 'wb')
        o.write(struct.pack('<I', n))
        new_offset = 4 + n * 8
        offset_padding = 16 - new_offset % 16
        if offset_padding == 16:
            offset_padding = 0
        new_offset += offset_padding
        for i in range(n):
            o.write(struct.pack('<I', new_offset))
            size = len(files[i])
            o.write(struct.pack('<I', size))
            new_offset += size + paddings[i]
        o.write(b'\x00' * offset_padding)
        for i in range(n):
            o.write(files[i] + b'\x00' * paddings[i])
        o.close()
        if compress and json_data[name] == 3:
            subprocess.run(['comptoe', '-c3', fname, fname + '.c'])
            os.remove(fname)
            os.rename(fname + '.c', fname)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        extract_pak1()
    elif sys.argv[1] == '2':
        insert_pak1()
    else:
        sys.exit(1)

import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def extract_scpk():
    mkdir('scpk_')
    for file in os.listdir('fpb'):
        f = open('fpb/%s' % file, 'rb')
        header = f.read(4)
        if header != b'SCPK':
            continue
        mkdir('scpk_/%s' % file[:-4])
        f.read(4)
        files = struct.unpack('<L', f.read(4))[0]
        f.read(4)
        sizes = []
        for i in range(files):
            sizes.append(struct.unpack('<L', f.read(4))[0])

        for i in range(files):
            o = open('scpk_/%s/%02d.bin' % (file[:-4], i), 'wb')
            o.write(f.read(sizes[i]))
            o.close()

        f.close()
        print (file)

if __name__ == '__main__':
    extract_scpk()

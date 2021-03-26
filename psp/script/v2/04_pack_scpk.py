import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def pack_scpk():
    mkdir('scpk_packed')
    
    for folder in os.listdir('scpk_/'):
        if os.path.isdir('scpk_/' + folder):
            sizes = []
            o = open('scpk_packed/%s.bin' % folder, 'wb')
            data = bytearray()
            for file in os.listdir('scpk_/' + folder):
                f = open('scpk_/%s/%s' % (folder, file), 'rb')
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
    pack_scpk()

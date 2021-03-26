import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def compress(data):
    compressed = zlib.compress(data, 7)
    header = b'\x04'
    header += struct.pack('<L', len(compressed))
    header += struct.pack('<L', len(data))
    return header + compressed

def compress_file(name):
    f = open(name, 'rb')
    data = compress(f.read())
    o = open(name + '.compressed', 'wb')
    o.write(data)
    f.close()
    o.close()
    print ("Compressed")
            
if __name__ == '__main__':
    compress_file('0000.bin.decompressed')

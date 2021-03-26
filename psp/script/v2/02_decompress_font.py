import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def decompress(data):
    if data[0] != 4:
        return data, False
    try:
        decompressed = zlib.decompress(data[0x9:], wbits = -15)
    except:
        return data, False
    return decompressed, True

def decompress_file(name):
    f = open(name, 'rb')
    data = decompress(f.read())[0]
    o = open(name + '.decompressed', 'wb')
    o.write(data)
    f.close()
    o.close()
    print ("Decompressed")

if __name__ == '__main__':
    decompress_file('0000.bin')
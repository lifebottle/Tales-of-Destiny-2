import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

def pack_fpb():
    sectors = [0]
    remainders = []
    buffer = 0

    o = open('new_file.fpb', 'wb')
    
    for name in os.listdir('fpb'):
        f = open('fpb/' + name, 'rb')
        size = os.path.getsize('fpb/' + name)
        remainder = 0x800 - (size % 0x800)
        if remainder == 0x800:
            remainder = 0
        o.write(f.read())
        o.write(b'\x00' * remainder)
        f.close()
        remainders.append(remainder)
        buffer += (size + remainder)
        sectors.append(buffer)
        print (name)

    #o = open('test.bin', 'wb')
    #for i in range(len(sectors)):
    #    o.write(struct.pack('<L', sectors[i] + remainders[i]))
        
    o.close()

if __name__ == '__main__':
    pack_fpb()

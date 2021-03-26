import sys, os, struct, zlib

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass
    
def get_pointers():
    f = open("ULJS00097.bin", 'rb')
    pointer_begin = 0x29531C
    pointer_end = 0x29E9AC
    f.seek(pointer_begin, 0)
    pointers = []
    dummies = []

    while f.tell() < pointer_end:
        p = struct.unpack('<L', f.read(4))[0]
        pointers.append(p)

    for i in range(len(pointers)-1):
        remainder = pointers[i] & 0x7FF
        start = pointers[i] & 0xFFFFF800
        end = (pointers[i+1] & 0xFFFFF800) - remainder

        if start == end:
            dummies.append(i)
        
    f.close()
    return pointers, dummies

def extract_fpb():
    f = open('FILE.FPB', 'rb')

    mkdir('FPB')

    pointers, dummies = get_pointers()
    
    for i in range(len(pointers)-1):
        remainder = pointers[i] & 0x7FF
        start = pointers[i] & 0xFFFFF800
        end = (pointers[i+1] & 0xFFFFF800) - remainder

        f.seek(start, 0)
        size = (end - start)
        #if size == 0:
        #    continue
        o = open('FPB/' + '%04d.bin' % i, 'wb')
        o.write(f.read(size))
        o.close()

    f.close()
            
if __name__ == '__main__':
    get_pointers()
    extract_fpb()
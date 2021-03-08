import binascii
import os
import re
import string
import struct

d = {}  #de-duplication dictionary
printable = ''.join((
    string.digits,
    string.ascii_letters,
    string.punctuation,
    ' '))
r = re.compile('linebreak|pagebreak')
with open(r'archive\0001.bin', 'r', encoding = 'cp932') as f:
    char_index = f.read()

def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def dic_update(s, n):
    if s == '':
        return ''
    if s in d:
        return d[s]
    else:
        d[s] = '{} {}'.format(basename, n)
        return ''

def decode(param):
    a2 = param
    a3 = 0x993F
    a1 = 0x9940
    if  a3 >= a2:
        a2 = a1
    a1 = a2 >> 8
    a0 = a2 & 0xFF
    t0 = True if a1 < 0xE0 else False
    v1 = a1 - 0x40
    a3 = a0 - 1
    a2 = True if a0 < 0x80 else False
    if t0 == False:
        a1 = v1 & 0xFFFF
    t1 = a1 - 0x99
    t0 = t1 & 0xFFFF
    v0 = 0xBB
    a1 = t0 * v0
    if a2 == False:
        a0 = a3 & 0xFFFF
    t2 = True if a0 < 0x5D else False
    v1 = a0 - 1
    if t2 == False:
        a0 = v1 & 0xFFFF
    t5 = a0 - 0x40
    t4 = t5 & 0xFFFF
    t3 = a1 + t4
    v0 = t3 & 0xFFFF

    return v0

def dump(filename):
    char_count = 0
    with open(filename, 'rb') as f:
        f.seek(8)
        text_offset = struct.unpack('<I', f.read(4))[0]
        f.seek(text_offset)
        s_start = f.tell()
        s_list = []
        s = []
        while True:
            b = f.read(1)
            if b == b'':
                break
            else:
                b = ord(b)
            if b == 0:
                s = ''.join(s)
                ref = dic_update(s, len(s_list))
                s_list.append((s, s_start - text_offset, ref))
    ##            print(''.join(s))
                s = []
                s_start = f.tell()
            elif chr(b) in printable:
                s.append(chr(b))
            elif (b >= 0x99 and b < 0xA1) or (b >= 0xE0 and b < 0xF0):
                c = (b << 8) + ord(f.read(1))
                s.append(char_index[decode(c)])
                char_count += 1
            elif b >= 0xA1 and b < 0xE0:
                s.append(struct.pack('B', b).decode('cp932'))
            elif b == 0x1:
                s.append('linebreak')
            elif b == 0x2:
                s.append('pagebreak')
            elif b in (0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB):
                num = struct.unpack('<I', f.read(4))[0]
                if b == 0x3:
                    s.append('{03:' + '{}'.format(num) + '}')
                elif b == 0x4:
                    s.append('{Color:' + '{}'.format(num) + '}')
                elif b == 0x5:
                    s.append('{Size:' + '{:0>3}'.format(num) + '}')
                elif b == 0x6:
                    s.append('{Num:' + '{}'.format(num) + '}')
                elif b == 0x7:
                    s.append('{Char:' + '{:0>2}'.format(num) + '}')
                elif b == 0x8:
                    s.append('{Item:' + '{}'.format(num) + '}')
                elif b == 0x9:
                    s.append('{Btn:' + '{:0>2}'.format(num) + '}')
                elif b == 0xB:
                    s.append('{0B:' + '{:0>2}'.format(num) + '}')
            elif b in (0x12, 0x14, 0x15, 0x16, 0x17, 0x18):
                b0 = b
                b1 = 0
                op = []
                while b1 not in (b'\xBC', b'\xC0'):
                    b1 = f.read(1)
                    op.append(b1)
                s.append('{' + hex(b0)[2:] + binascii.hexlify(b''.join(op)).decode('ascii') + '}')
            elif b == 0x83:
                s.append('{93' + binascii.hexlify(f.read(1)).decode('ascii') + '}')
            elif b == 0x93:
                s.append('{93' + binascii.hexlify(f.read(4)).decode('ascii') + '}')
            elif b == b'':
                break
            else:
                print(hex(f.tell()), hex(b))
                raise ValueError
    out = []
    for i, (s, s_start, ref) in enumerate(s_list):
        out.append('{}\t'.format(str(i)))
        s0 = []
        s1 = []
        while True:
            m = re.search(r, s)
            if m == None:
                break
            s0.append(s[:m.start()])
            s1.append(s[m.start():m.end()])
            s = s[m.end():]
        s0.append(s)
        s1.append('')
        s2 = [hex(s_start)] + [''] * (len(s0) - 1)
        s3 = [ref] + [''] * (len(s0) - 1)
##Uncomment (and comment out the other one) to dump string offsets in addition
##        out.append('\n\t'.join('\t'.join(x) for x in zip(s2, s0, s3, s1)))
        out.append('\n\t'.join('\t'.join(x) for x in zip(s0, s3, s1)))
        out.append('\n')
    return ''.join(out), char_count

def dump_all():
    global basename
    char_count = []
    ensure_dir('script')
    for root, dirs, files in os.walk('SCPK'):
        for file in files:
            if '.SCED' in file:
                basename = os.path.split(root)[-1]
                filename = os.path.join(root, file)
                print(filename)
                try:
                    s, char_count0 = dump(filename)
                except Exception as err:
                    print(err)
                    continue
                char_count.append((basename, char_count0))
                with open(r'script\{}.tsv'.format(basename), 'w', encoding = 'utf-8') as f:
                    f.write(s)
    with open('totals.tsv', 'w', encoding='ascii') as f:
        f.write('\n'.join('{}\t{}'.format(a, b) for a, b in char_count))

dump_all()

#for a single file
##basename = '6470'
##s, char_count = dump(r'SCPK\6470\20.SCED')
##with open('output.tsv', 'w', encoding='utf-8') as f:
##    f.write(s)

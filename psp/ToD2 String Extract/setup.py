import glob
import os
import struct
import subprocess
import sys
import zlib

#import ISO_extract

compressed_s = {True: 'compressed', False: 'raw'}

def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def decompress(data):
    if data[0] == 4:
        compressed = True
        try:
            data = zlib.decompress(data[0x9:], wbits = -15)
        except zlib.error:
            compressed = False
    else:
        compressed = False
    return data, compressed

def get_ext(data):
    ext = 'bin'
    if data[:4].isalpha():
        ext = data[:4].decode('ascii')
        if ext == 'VAGp':
            ext = 'vag'
    elif data[:3].isalpha():
        ext = data[:3].decode('ascii')
        if ext == 'MIG':
            ext = 'GIM'
    elif data[0:4] == b'\x89PNG':
        ext = 'png'
    elif data[0:1].isalpha() and data[0x10:0x11] == b'.':
        ext = 'arc'
    elif data[0:4] == b'MIG.':
        ext = 'GIM'
    return ext

if len(sys.argv) == 1:
    print('Run using provided .bat file')
    quit()

print('ToD2 PSP ver. archive unpack')
print('deceboot is by NoOnee at romhacking.net')
print('the rest of this tool is by me, flamethrower')
print('and modifications by pnvnd')

#print('\nStarting ISO extractions...')
ensure_dir('archive')
#ISO_extract.ISO_extract(sys.argv[1], r'USRDIR\file.fpb')

#EBOOT
#ensure_dir('EBOOT')
#ISO_extract.ISO_extract(
#    sys.argv[1], r'SYSDIR\EBOOT.BIN', None, target=r'EBOOT')
#
#print('\nStarting EBOOT decryption...')
#subprocess.run([r'bin\deceboot.exe',
#                r'EBOOT\EBOOT.BIN', r'EBOOT\ULJS00097.BIN'])
#os.remove(r'EBOOT\EBOOT.BIN')

ensure_dir('archive')

print('\nStarting extraction of main archive file.fbp...')
offsets = []
with open(r'EBOOT\ULJS00097.BIN', 'rb') as f:
    f.seek(0x29531C)
    while f.tell() < 0x29e9ac:
        offsets.append(struct.unpack('<I', f.read(4))[0])

TOC = []
with open('file.fpb', 'rb') as f:
    for i, (start, end) in enumerate(zip(offsets, offsets[1:])):
        remainder = start & 0x7FF
        start_LBA = start >> 11
        start_pos = start & 0xFFFFF800
        end_LBA   = end >> 11
        end_pos   = (end & 0xFFFFF800) - remainder
        fsize      = end_pos - start_pos
        
        f.seek(start_pos)
        if end_pos - start_pos == 0:
##            print('{}: zero-length data'.format(i))
            TOC.append((str(i), 'dummy'))
            continue
##        print(hex(start_pos), hex(end_pos), hex(remainder))
        data = f.read(fsize)
        data, compressed = decompress(data)
        ext = get_ext(data)
        fname = r'archive\{:0>4d}.{}'.format(i, ext)
        with open(fname, 'wb') as g:
            g.write(data)
        TOC.append((str(i), compressed_s[compressed]))
                
print('\nStarting extraction .SCPK files...')
with open('TOC.tsv', 'w') as f:
    f.write('\n'.join('\t'.join(x) for x in TOC))

for file in glob.glob(r'archive\*.SCPK'):
    basename = file.split('\\')[1].split('.')[0]
    ensure_dir(r'SCPK\{}'.format(basename))
    with open(file, 'rb') as f:
        f.seek(8)
        num_files, dummy = struct.unpack('<II', f.read(8))
        TOC = struct.unpack('<' + 'I' * num_files, f.read(4 * num_files))
        for i, size in enumerate(TOC):
            data, compressed = decompress(f.read(size))
            ext = get_ext(data)
            with open(r'SCPK\{}\{:0>2d}.{}'.format(basename, i, ext), 'wb') as g:
                g.write(data)

print('\nStarting string dumping (.SCED files)...')
import string_dump  #This runs this

print('\nOperation finished.')

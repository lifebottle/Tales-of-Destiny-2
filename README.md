# Tales of Destiny 2 (PS2)
This project is an attempt at an open-source translation for Tales of Destiny 2, both for PS2 and PSP.
  
To be clear, this is *not* for Tales of Eternia (PSP) or Tales of Destiny II (PS1).  
After starting and handing off an open-source project for [Tales of Destiny Director's Cut](https://github.com/furiousg4m3r/Tales-of-Destiny-DC "Tales of Destiny DC") (PS2), the aim of this project is have tools and resources available to complete a patch for Tales of Destiny 2 (PS2), a "sequel" to the first game.  


This repository aims to collect all known information about this game in order to create a patch.  

Join on Discord: https://discord.gg/HZ2NFjpedn  

Spreadsheet with Info: https://docs.google.com/spreadsheets/d/1UVaEjK0o-V1-3atPHfRRw2q9QQcCzPCpr4GXJ2MLvvg

## Wanted Items

1. Tool to extract and re-insert the fonts
1. Tool to extract the `TM2` files
1. `abcde`, `cartographer`, and `atlas` script to dump and insert menu text



## FILE.FPB (PS2) INFO
1. The pointer table is in the `SLPS_251.72` file starting at `0xDD320`
1. Each entry of the table consists of (A) a 26-bit offset -> the file offset inside `SLPS_251.72`


## SLPS_251.72

Offset   | Description | Notes
---------|-------------|----------------------
00000000 | ELF Start   | Beginning of file
000CA328 | Font (.tm2) | Extract and use comptoe.exe
000C9D41 | Font Map    | Map lowercase to font

### Mapping Lowercase Letters
1. Edit `.tm2` from `0x0CA328` and replace some Hiragana
2. Go to `0x0C9D41` in the SLPS_251.72 file
3. It should have a `0x17`
4. That's the glyph index for lowercase "a"
5. Replace that with `0x31` which is "ぁ"
6. And just follow the sequence up until `0x4B`

## FILE.FPB (PSP) INFO
1. FILE.FPB has information to unpack the files inside `EBOOT.BIN`
1. Decrypted `EBOOT.BIN` is also known as `ULJS00097.BIN`
1. Each entry of the table consist of (A) a 21-bit offset -> the file offset inside `FILE.FBP` and (B) 11-bits for flags -> Compression, file type, etc...
1. In order to extract the big file, one would calculate each file size based on the next file's offset. 
1. That is enough to extract the whole FBP. Reversing the process, it would be easy to repack it.
1. The pointer table starts at the `0x44`, which references the very first file in the package (the font).
1. 21-bits are enough to reference any file in the package. That's because they represent not a byte offset, but a sector in the disc. 
1. The ISO9660 standard uses `0x0800` bytes sectors. The way to work with them actually depends of the way you think it though:
1. If you shift 11-bits from data, you'll get the file sector, so you can get the byte offset multiplying that value by `0x0800`.
1. Since these 21-bits take the most significant part of the data, you can apply a `0xFFFFF800` mask to it, to directly get the byte offset to the file

### Implementation
```
unsigned int fileSize = (nextSector - currentSector) * 0x0800 - remainder;
```
For example, to extract the font we would look at the following data:

- First file -> Sector 0, remainer 0x044C
- Second file -> Sector 92

- Offset = 0 * 0x0800 = 0
- Size = (92 - 0) * 0x0800 - 0x044C = 48BB4

And that should cover extracting the FBP.


## ULJS00097.BIN / EBOOT.BIN

Offset   | Description | Notes
---------|-------------|----------------------
00000000 | ELF Start   | Beginning of file



## Resources

- https://gbatemp.net/threads/romhacking-in-tales-of-destiny-2.373960/
- https://gbatemp.net/threads/romhacking-in-tales-of-destiny-2.373960/page-3
- https://pastebin.com/fCVPLUP4
- https://www.mediafire.com/file/e44c1ksxl7a17z8/ToD2_String_Extract_v1.7z/file
- https://github.com/talestra/talestra/tree/master/compto


## Hacker Note 1
The main difference between PSP and PS2 versions is the compression system. While PS2 uses a mixture of LZSS and RLE, PSP uses zLib. The format of the inner files should be identical.

Before compression, most interesting files are packed using a SCPK header. There is always one initial file (background), then a descriptor table (with one entry per additional file), and then the rest of the files (a set of sprite + amination files, and finishing, a script file).

Background and sprite files use 8-bit indexed RGBA color, reaching a maximum of possible 256 color per palette. Note that the graphic format does support multiple palettes for a same pixel matrix.

The script files use the SCED signature, and contain two main sections:

- The code section, which governs the scripted logic.
- The text section, which contains the strings coded in a custom format.

The ideal way to parse the SCED is to decompile the code section, which contains pointers to the text section.

The important bit about the text is that, once decoded, the string consists in an array of font indices.

## Hacker Note 2
The `TM2` font inside `SLPS_251.72` works the following way:
- there are ten 4-bit palettes at the begining
- the number of palette seems to be at byte 0x05
- each palette is then `0x40` bytes
- each palette comes with a `0x10` bytes sub-header, so `0x50` per palette
- the file header is `0x10` bytes too
- after the palette array, there is another `0x10` subheader for the pixel matrix
- this one includes the resolution (128 x 512 in this case)
- the matrix size is the rest of the data in the file
- 128 x 512 / 2 (divided by 8 because the matrix is 4 bits)
- on a PSP 4-bit graphic, the lower nibble corresponds to the first pixel out of both!
And that accounts for the remaining 32768 bytes of the file

## Hacker Note 3
To extract font image from `0018.bin` (PS2) and `0000.bin` (PSP):
- take every 4 bits and draw a pixel any level from black to white according to it
- for example 0 -> black and 15 -> white
- then give it a width (I don't remember exacly, but it was a power of 2)
- That will effectively give you the font graphic file
- edit it, and reverse everything
- also update the font descriptor to keep it consistent with your editions
- though the game (probably) doesn't actually use the font descriptor, it's only useful to decode the text by a romhacker

## Screenshots

![SLPS_251.72](https://raw.githubusercontent.com/pnvnd/Tales-of-Destiny-2/main/tod2_slps_base.png)

## Credits
- Thanks to the Temple of Tales Translations team (http://temple-tales.ru/translations.html) for providing tools to extract the skits and scenarios
- Thanks to @alizor for creating the Python scripts to extract and repack both PS2 and PSP versions of the game
- Thanks to SkyBladeCloud from GBATemp for tips on how the game / file works
- Thanks to flamethrower / flame1234 from GBATemp for having Python scripts available to extract the PSP version of the game

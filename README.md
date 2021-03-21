# Tales of Destiny 2 (PS2)
This project is an attempt at an open-source translation for Tales of Destiny 2 (PS2).  
To be clear, this is *not* for Tales of Eternia (PSP) or Tales of Destiny II (PS1).  
After starting and handing off an open-source project for [Tales of Destiny Director's Cut](https://github.com/furiousg4m3r/Tales-of-Destiny-DC "Tales of Destiny DC") (PS2), the aim of this project is have tools and resources available to complete a patch for Tales of Destiny 2 (PS2), a "sequel" to the first game.  
This repository aims to collect all known information about this game in order to create a patch.  

Join on Discord: https://discord.gg/HZ2NFjpedn

## Wanted Items

1. Any existing tools, source code, repositories, but also available to be open-sourced in this repository
2. PS2 memory card file or save files at as many different save points as possible
3. Source code to extract `FILE.FPB` (1.41 GB)
4. A TBL file or mapping of Hex to Japanese to start dumping text, or source code to decode
5. Any other advice that can be offered to get all the tools available for patch making

## SLPS_251.72

Offset   | Description | Notes
---------|-------------|----------------------
00000000 | ELF Start   | Beginning of file

## FILE.FPB (PSP)

### Hints
1. Following instructions are for PSP, scripts doesn't work with PS2 so far
2. FILE.FPB does not include information to unpack the files inside
3. the pointer table seems to be in the slps file, address DD320 - it uses 26 bits instead of 21 from the psp
4. Each entry of the table consist of (A) a 21-bit offset -> the file offset inside FILE.FBP and (B) 11-bits for flags -> Compression, file type, etc...
5. In order to extract the big file, one would calculate each file size based on the next file's offset. 
6. That is enough to extract the whole FBP. Reversing the process, it would be easy to repack it.
7. The pointer table starts at the `0x44`, which references the very first file in the package (the font).
8. 21-bits are enough to reference any file in the package. That's because they represent not a byte offset, but a sector in the disc. 
9. The ISO9660 standard uses `0x0800` bytes sectors. The way to work with them actually depends of the way you think it though:
10. If you shift 11-bits from data, you'll get the file sector, so you can get the byte offset multiplying that value by `0x0800`.
11. Since these 21-bits take the most significant part of the data, you can apply a `0xFFFFF800` mask to it, to directly get the byte offset to the file

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

## Resources

- https://gbatemp.net/threads/romhacking-in-tales-of-destiny-2.373960/
- https://gbatemp.net/threads/romhacking-in-tales-of-destiny-2.373960/page-3
- https://pastebin.com/fCVPLUP4
- https://www.mediafire.com/file/e44c1ksxl7a17z8/ToD2_String_Extract_v1.7z/file
- https://github.com/talestra/talestra/tree/master/compto

## Screenshots

![SLPS_251.72](https://raw.githubusercontent.com/pnvnd/Tales-of-Destiny-2/main/tod2_slps_base.png)

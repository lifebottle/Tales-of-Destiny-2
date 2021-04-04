--------------------------------
Tales of Destiny 2 TM2 Converter
--------------------------------
Generously donated by the Temple of Tales Translation Team: http://temple-tales.ru/translations.html


************
Requirements
************
1. TalesOfDestinyTm2Converter.exe
2. ttemma.Helpers.dll


*****
Usage
*****
To extract PNG from TM2 file, drag and drop the .TM2 file into extract.bat or use this command:
TalesOfDestinyTm2Converter.exe -e 00020.tm2

To repack .TM2 file, a PNG file with the same file name as the .TM2 must be present.
For example, to repack 00020.tm2 you also need 00020.tm2.png in the same directory.
Then, drag and drop the .TM2 file into repack.bat or use this command:
TalesOfDestinyTm2Converter.exe -r 00020.tm2

*****
Notes
*****
Used "apphost-extract" to extract the .NET assembly embedded in the runtime, and then decompiled with a normal decompiler like IlSpy.

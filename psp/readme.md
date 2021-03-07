# ToD2 String Extract v1 by flame1234
Original python script found here:  
https://gbatemp.net/threads/romhacking-in-tales-of-destiny-2.373960/page-3#post-7669391

Link to download the tool:  
https://www.mediafire.com/file/e44c1ksxl7a17z8/ToD2%20String%20Extract%20v1.7z

## Instructions
This script has only been tested with the PSP version of Tales of Destiny 2
1. Download and extract ToD2 String Extract v1.7z
2. Open command prompt and enter `bin\deceboot.exe D:\PSP_GAME\SYSDIR\EBOOT.BIN ..\EBOOT\ULJS00097.BIN`
3. This will decrupt the PSP `EBOOT.BIN` file, saved to the folder where the tool was extracted, and renamed to `ULJS00097.BIN`
4. Copy `D:\PSP_GAME\USRDIR\file.fpb` to the folder where the tool was extracted under the `EBOOT` folder
5. Modify `setup.py` and comment out (with `#`) the following lines referencing `ISO_extract`: 8, 54-64, 
6. Drag and drop `TOD2.ISO` into the `_setup.bat` to start extracting `file.fpb` and extract text
7. Alternatively, open a command prompt and enter `python setup.py`

## Skits (not verified)
1. Get `pakcomposer` and `comptoe` and extract `.bin` files from 0213.bin to 1457.bin as `.pak1` files.
2. Move all of the `.SCED` files into a folder, `SCED` for example.
3. Modify `string_dump.py` line 156 and change `SCPK` to `SCED`
4. Open command prompt and enter `python string_dump.py` to get skit text dumped

## Help Wanted
1. Need script to reinsert `.tsv` file into `.SCED`
2. Need script to repack archive back into file.fpb

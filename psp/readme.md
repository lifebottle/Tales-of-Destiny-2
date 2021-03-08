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

## PAK0 FIles
1. 0213.bin - 1457.bin
2. 6333.bin - 6467.bin
3. 7310.bin
4. 8333.bin - 9565.bin

## PAK1 Files
1. Get `pakcomposer` and `comptoe` and extract `.bin` files from:
2. 0213.bin to 1457.bin (skits?)
3. 8331.bin to 9224.bin (enemies?)

## PAK3 Files
1. 0002.bin
2. 8331.bin - 9354.bin (enemies?)

## Help Wanted
1. Need script to reinsert `.tsv` file into `.SCED`
2. Need script to repack archive back into file.fpb
3. Need to confirm 8331.bin and up to see if it should be pak0, pak1, or pak3

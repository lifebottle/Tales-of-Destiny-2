#Tales of Destiny 2 (PS2) Tool

##Usage
1.  Copy SLPS_251.72 and FILE.FPB to this directory

2.  Run 01_extract_files.bat or "python tod2_ps2.py 1"
2a. This will extract files to FPB folder
2b. Then it will extract SCED from SCPK files in FPB folder
2c. Finally extract text from SCED to TXT folder

*********
SCENARIOS
*********

3.  Create TXT_EN folder and copy translated text files here
4.  Run 02_insert_files.bat or "python tod2_ps2.py 2" to insert scenario text to SCED_NEW and re-pack SCPK to SCPK_PACKED folder
5.  Copy files from SCPK_PACKED to FPB folder

*****
SKITS
*****

6.  Run 11_unpack_folders.bat or "python unpack_folders.py".
6a. This will create a FILE folder and organize files in FPB by extension, and will decompress with comptoe.exe if needed.

7.  Copy 00056.pak1 to 01298.pak1 from FILES/pak1 to PAK1 folder
8.  Run A_extract_pak1.bat or "python pak1.py" 1 to unpack PAK1 skit files
9.  Run B_move_skits.bat to move SCED skit files to SKITS\SCED folder (create folder if needed)
10. In the SKITS folder, run C_extract_sced.bat or "python tod2_ps2.py 7" to extract skit text to SKITS\TXT folder
11. Create TXT_EN folder and copy translated skit text to this folder
12. In the SKITS folder, run D_insert_sced.bat or "python tod2_ps2.py 8" to insert translated skit text to SCED file in SKITS\SCED_NEW folder
13. In the main folder, run E_copy_sced_pak1.bat to move skit text in SKITS\SCED_NEW folder to PAK1\##### folder
14. In the main folder, run F_insert_pak1.bat to repack PAK1 files to "pak1_packed" folder and compress with comptoe.exe
15. Copy PAK1 files from "pak1_packed" folder to FPB Folder.

***
FPB
***
16. Create a copy of SLPS_251.72 used to extract FILE.FPB and rename it to "new_SLPS_251.72"
17. Run 03_pack_fpb.bat or "python tod2_ps2.py 3" to get "FILE_NEW.FPB" and an updated "new_SLPS_251.72" file
18. Run 04_insert_font.bat or "python tod2_ps2.py 4" to insert font.bin and update lowercase letter mapping (optional)
19. Copy/move and rename "FILE_NEW.FPB" to "FILE.FPB" and "new_SLPS_251.72" to "SLPS_251.72" to replace in game ISO

***
TBL
***
20. Run 10_export_tbl.bat or "python tod2_ps2.py 10" to dump TBL file from TBL.JSON for use with abcde, Cartographer, Atlas, etc.

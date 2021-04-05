setlocal enabledelayedexpansion
set folderpath=%~dp0SKITS
for %%f in (%folderpath%\SCED_NEW\*.sced) do (
  set "foldername=%%~nf"
  copy "%%f" "%~dp0PAK1\!foldername:~0,-3!"
) 
pause
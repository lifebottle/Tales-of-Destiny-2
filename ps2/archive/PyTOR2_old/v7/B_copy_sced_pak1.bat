setlocal enabledelayedexpansion
set folderpath=%~dp0SKITS
for %%f in (%folderpath%\SCED_NEW\*.sced) do (
  set "foldername=%%~nf"
  move "%%f" "%~dp0PAK1\!foldername:~0,-5!"
) 
pause
@echo off
if [%1]==[] goto error

echo Extracting files...
cd /d %~dp0
py -3 setup.py %1
echo Finished.
goto :end

:error
echo Please drag and drop your original ISO over _extract.bat
echo instead of double clicking.
echo.

:end
pause
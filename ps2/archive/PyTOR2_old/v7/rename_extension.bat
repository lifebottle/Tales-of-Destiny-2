for /f "delims=" %%i in ('dir /a-d/b/s *.pak1_bak') do ren "%%i" "%%~ni.pak1"
pause
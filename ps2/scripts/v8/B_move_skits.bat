for /r "%~dp0PAK1" %%i in (*.sced) do (
	move /y "%%~i" "%~dp0SKITS\SCED"
)
pause
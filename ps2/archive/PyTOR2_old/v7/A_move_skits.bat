for /r "%~dp0PAK1/pak1" %%i in (*.sced) do (
	move /y "%%~i" "%~dp0SKITS"
)
pause
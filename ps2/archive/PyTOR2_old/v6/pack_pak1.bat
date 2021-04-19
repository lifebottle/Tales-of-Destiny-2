for %%i in (*) do pakcomposer.exe -c "%%i" -1 -x -u -v -tod2_ps2_skit_padding
REM remove -tod2_ps2_skit_padding for non-skit files
pause
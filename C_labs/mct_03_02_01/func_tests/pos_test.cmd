@ECHO OFF

IF "%1"=="" ECHO NOT ENOUGH PARAMETERS... & GOTO :END

drmemory -lib_blacklist "*" -batch -prefix_style 2 -logdir ..\out\ -- ..\app.exe <pos_%~1_in.txt >out.txt
IF %ERRORLEVEL% NEQ 0 ECHO POS TEST %~1 ::FAIL:: RETURN CODE IS NOT ZERO... & GOTO :END

FC /N pos_%~1_out.txt out.txt

DEL out.txt

:END

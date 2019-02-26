@echo off
setlocal

set EXECUTABLE=%1
set VFXTEST_ROOT=%2
set SETTINGS_ROOT=%3
set DEBUG_MODE=%4

set COMMAND=%EXECUTABLE% -command "source maya_wrapper; DoIt()"

IF "%DEBUG_MODE%"=="True" (
    echo.
    echo [DBG] Resulting Command:
    echo       ------------------
    echo       %COMMAND%
    echo.
    echo.
    echo.
)

set MAYA_APP_DIR=%SETTINGS_ROOT%/maya.vfxtest
set MAYA_SCRIPT_PATH=%~dp0;%VFXTEST_ROOT%\wrapper_scripts
set PYTHONPATH=%~dp0;%VFXTEST_ROOT%;%VFXTEST_ROOT%\wrapper_scripts;%SETTINGS_ROOT%\virtualenv_python2.x\Lib\site-packages;%PYTHONPATH%
set MAYA_PLUG_IN_PATH=
set MAYA_MODULE_PATH=

%COMMAND%

endlocal

rem Maya _always_ seems to be setting the %ERRORLEVEL% to 1.
rem Soooo we ignore it...
exit /B 0

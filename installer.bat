@echo off
setlocal enabledelayedexpansion

:: check for admin
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% NEQ 0 (
    echo requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

set repo_url=https://raw.githubusercontent.com/fyresoftworks/chainsaw/main/chainsaw.py
set install_dir=%USERPROFILE%\chainsaw
set bin_dir=%USERPROFILE%\chainsaw_bin
set bat_file=%bin_dir%\chainsaw.bat

:menu
cls
echo chainsaw installer
echo.
echo 1. install
echo 2. uninstall
echo 3. exit
echo.
set /p choice=choose an option:

if "%choice%"=="1" goto install
if "%choice%"=="2" goto uninstall
if "%choice%"=="3" exit
goto menu

:install
echo downloading chainsaw.py...
if not exist "%install_dir%" mkdir "%install_dir%"
curl -s -o "%install_dir%\chainsaw.py" "%repo_url%"

if errorlevel 1 (
    echo failed to download chainsaw.py
    pause
    exit /b 1
)

echo creating chainsaw.bat...
if not exist "%bin_dir%" mkdir "%bin_dir%"
(
    echo @echo off
    echo python "%install_dir%\chainsaw.py" %%*
) > "%bat_file%"

echo checking if path is set...

:: fetch current user path
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do (
    set current_path=%%b
)

echo current path: !current_path!
echo !current_path! | find /i "%bin_dir%" >nul
if errorlevel 1 (
    set new_path=!current_path!;%bin_dir%
    reg add "HKCU\Environment" /v Path /t REG_EXPAND_SZ /d "!new_path!" /f >nul
    echo path updated
) else (
    echo path already contains chainsaw_bin
)

echo.
echo chainsaw installed successfully
echo you may need to log out and back in to apply path changes
pause
exit /b

:uninstall
echo removing chainsaw...
if exist "%bat_file%" del "%bat_file%"
if exist "%bin_dir%" rmdir /s /q "%bin_dir%"
if exist "%install_dir%" rmdir /s /q "%install_dir%"

:: clean PATH
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do (
    set old_path=%%b
)

set new_path=
for %%a in ("!old_path:;=";"!") do (
    set part=%%~a
    echo !part! | find /i "%bin_dir%" >nul
    if errorlevel 1 (
        if defined new_path (
            set new_path=!new_path!;!part!
        ) else (
            set new_path=!part!
        )
    )
)

reg add "HKCU\Environment" /v Path /t REG_EXPAND_SZ /d "!new_path!" /f >nul

echo uninstalled chainsaw
echo you may need to log out and back in to apply path changes
pause
exit /b

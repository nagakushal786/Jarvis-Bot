@echo off
setlocal EnableDelayedExpansion
set ADB_PATH="D:\platform-tools-latest-windows\platform-tools\adb.exe"

echo Restarting the ADB server
%ADB_PATH% kill-server
%ADB_PATH% start-server

echo Disconnecting old connections...
%ADB_PATH% disconnect

echo Setting up connected device...
%ADB_PATH% tcpip 5555

echo Waiting for device to initialize...
rem Universal delay without external commands
for /L %%i in (1,1,10000) do rem > nul

echo Finding device IP...
set ip=
rem Get IP using pure batch methods
for /F "tokens=2 delims=:" %%a in ('%ADB_PATH% shell ifconfig 2^>^&1 ^| findstr /B /C:"      inet"') do (
    for /F "tokens=1" %%b in ("%%a") do set ip=%%b
)

if not defined ip (
    echo Alternative method to find IP...
    for /F "tokens=2" %%a in ('%ADB_PATH% shell ip route 2^>^&1 ^| findstr /C:"src"') do set ip=%%a
)

if defined ip (
    echo Device IP found: !ip!
    echo Connecting to !ip!...
    %ADB_PATH% connect !ip!
) else (
    echo Failed to find device IP automatically
    echo Attempting manual connection...
    rem Hardcoding the current IP address of my phone
    %ADB_PATH% connect 192.168.1.10:5555
)

endlocal
exit /b
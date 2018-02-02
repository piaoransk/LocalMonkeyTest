@echo off 
color a
title ReleaseAdbPort
echo ======================
echo ***  2017-12-4***
echo ***     v1.0.0     ***
echo ======================
echo ---------------------------
echo Checking adb port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "5037""`) do (   
if not "%%a" =="0" call :ReleasePort %%a
)
echo ---------------------------
echo adb port has been released!
echo ---------------------------


exit

:ReleasePort
TASKKILL /f /PID %1
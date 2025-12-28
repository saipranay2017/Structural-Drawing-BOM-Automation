@echo off

cd ..\..
cd /d E:\SBOM\SBOM_Deployment_Mode

call Project_Environment\Scripts\activate
if errorlevel 1 (
    echo Activation failed!
    pause
    exit /b
)

python mapp.py
if errorlevel 1 (
    echo Python script failed!
    pause
    exit /b
)

pause


@echo off

cd ..\..
cd /d E:\SBOM\SBOM_project_deployment_mode

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


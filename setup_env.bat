@echo off
title AI Coding Workshop - Setup
chcp 65001 >nul

rem 1) Check Python (also catches the fake python.exe from Microsoft Store)
python --version >nul 2>nul
if errorlevel 1 (
    echo [!] Python not found.
    echo     Download page will open: https://www.python.org/downloads/
    echo     IMPORTANT: tick  "Add Python to PATH"  when installing.
    echo     After installing, double-click this file again.
    start https://www.python.org/downloads/
    pause
    exit /b 1
)

rem 2) Always run from the project folder
cd /d "%~dp0"

rem 3) Main script (all Chinese messages are printed by setup_env.py)
python setup_env.py %*

pause

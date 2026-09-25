@echo off
title Smart Uzhavan AI Doctor
color 0A
echo ===================================================================
echo             SMART UZHAVAN AI DOCTOR (உழவன் AI)
echo      Crop Disease Scanner & Tamil Human Voice Assistant
echo ===================================================================
echo.

:: 1. Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please download and install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b
)

:: 2. Setup Virtual Environment
if not exist .venv (
    echo [Step 1/3] Creating virtual environment (.venv)...
    python -m venv .venv
)

:: 3. Install Requirements
echo [Step 2/3] Verifying dependencies...
call .venv\Scripts\activate.bat
pip install -r requirements.txt --quiet

:: 4. Launch Streamlit
echo.
echo [Step 3/3] Launching Uzhavan AI Doctor in your browser...
echo ===================================================================
echo App URL: http://localhost:8501
echo Close this terminal window to stop the server.
echo ===================================================================
streamlit run app.py
pause

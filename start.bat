@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    py -3 -m venv .venv
    if errorlevel 1 goto failed
)
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
if not exist ".env" copy /y ".env.example" ".env" >nul
echo.
echo Open http://127.0.0.1:5000 in your browser.
echo Put your Gemini key in .env, then restart this window.
echo Press Ctrl+C to stop.
".venv\Scripts\python.exe" app.py
if errorlevel 1 goto failed
exit /b 0
:failed
echo Startup failed. Check Python 3.10+ and your network connection.
pause
exit /b 1

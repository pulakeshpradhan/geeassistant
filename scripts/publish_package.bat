@echo off
echo Building package...
python -m build
if %errorlevel% neq 0 exit /b %errorlevel%

echo Uploading to PyPI...
twine upload dist/*
pause

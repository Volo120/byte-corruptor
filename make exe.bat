@echo off
set appName=byte corruptor
pyinstaller .\main.py --onefile -n "%appName%" -F -w
cd ./dist
move ./*.exe ../
cd ..
rd /s /q __pycache__
rd /s /q build
rd /s /q dist
del /q "%appName%.spec"
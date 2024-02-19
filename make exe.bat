@echo off
pyinstaller .\main.py -n "Corrupter" -F
cd ./dist
move ./*.exe ../
cd ..
rd /s /q __pycache__
rd /s /q build
rd /s /q dist
del /q "Corrupter.spec"

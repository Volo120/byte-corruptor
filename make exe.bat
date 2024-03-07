@echo off
pyinstaller .\main.py --onefile -n "Corruptor" -F -w
cd ./dist
move ./*.exe ../
cd ..
rd /s /q __pycache__
rd /s /q build
rd /s /q dist
del /q "Corruptor.spec"
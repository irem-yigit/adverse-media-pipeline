@echo off
chcp 65001
cd C:\Users\yigit\projects\backend\adverse-media-pipeline
C:\Users\yigit\projects\backend\adverse-media-pipeline\venv\Scripts\python.exe -X utf8 main.py >> logs\daily.log 2>&1

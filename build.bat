@echo off
setlocal enabledelayedexpansion

:: 1. Список папок с ресурсами
set folders="diagramm_ychet" "image" "image_inform" "kartinka" "logo" "static" "templates" "diagramms" "str_tovar"

:: 2. Собираем все --add-data в одну переменную
set add_data=
for %%f in (%folders%) do (
    set add_data=!add_data! --add-data "%%~f\*;%%~f"
)

:: 3. Добавляем отдельные не-Python файлы
set add_data=!add_data! --add-data "requirements.txt;."

:: 4. Основная команда сборки (ВАЖНО: только ОДИН основной скрипт)
pyinstaller --onefile --windowed %add_data% glavnay.py

@pause
@echo off
cd /d %~dp0

REM Открытие окна выбора файла
set "fileFilter=UI Files (*.ui)|*.ui|All Files (*.*)|*.*"
set "defaultFile="
set "dialogTitle=Выберите UI-файл"


for /f "delims=" %%I in ('powershell -Command "Add-Type -AssemblyName System.Windows.Forms; $dlg = New-Object System.Windows.Forms.OpenFileDialog; $dlg.InitialDirectory = Get-Location; $dlg.Filter = '%fileFilter%'; $dlg.Title = '%dialogTitle%'; $dlg.FileName = '%defaultFile%'; $dlg.ShowDialog() | Out-Null; $dlg.FileName"') do set "selectedFile=%%I"

if not "%selectedFile%"=="" (
    echo Выбран файл: %selectedFile%
    
)
    
    REM Выполнение команды pyuic6
    pyuic6 -x "%selectedFile%" -o .\output.py
) else (
    echo Файл не выбран.
)

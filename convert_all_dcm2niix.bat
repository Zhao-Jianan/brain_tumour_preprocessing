@echo off
setlocal enabledelayedexpansion


:: 设置输入和输出根目录
set "INPUT_ROOT=C:\Users\ajhz839\workwork\Data\2022_GBM_PD_MRI_DICOM\20221130_36656053_KYJ"
set "OUTPUT_ROOT=C:\Users\ajhz839\workwork\Data\NIfTI\20221130_36656053_KYJ"

:: 遍历所有子文件夹
for /d /r "%INPUT_ROOT%" %%I in (*) do (
    if exist "%%I\*.dcm" (
        set "INPUT_PATH=%%I"

        :: 取当前子文件夹的名字作为输出子目录
        for %%F in ("%%I") do set "FOLDER_NAME=%%~nxF"
        set "OUTPUT_PATH=%OUTPUT_ROOT%\!FOLDER_NAME!"

        echo Converting:
        echo Input:  %%I
        echo Output: !OUTPUT_PATH!
        echo ----------------------------

        if not exist "!OUTPUT_PATH!" (
            mkdir "!OUTPUT_PATH!"
        )

        :: 调用 dcm2niix
        dcm2niix -z y -o "!OUTPUT_PATH!" "%%I"
    )
)

echo All conversions completed.
pause

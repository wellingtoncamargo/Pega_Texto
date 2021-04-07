from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["Tesseract-OCR"]}

setup(
    name="Pega_Texto",
    version = "1.0.3",
    description = ".py to .exe",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Pega Texto.py")])
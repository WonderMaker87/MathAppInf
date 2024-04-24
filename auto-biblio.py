#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import sys

def install_and_import(package):
    try:
        __import__(package)
        print(f"Le package {package} est déjà installé.")
    except ImportError:
        print(f"Installation du package {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        __import__(package)
        print(f"Le package {package} a été installé.")

# Liste des packages nécessaires pour votre application
packages = [
    "numpy", "PIL", "csv", "scipy", "matplotlib", "cv2", "skimage", 
    "sklearn", "webcolors", "pandas", "tkinter", "colorsys"
]

for package in packages:
    install_and_import(package)

print("Tous les packages nécessaires sont installés.")

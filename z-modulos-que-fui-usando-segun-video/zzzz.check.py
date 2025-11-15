# *** CHAT! dame la descripcion mas profesional, abarcativa y entendible posible en formato md, lista apra agregar a mi archivo md, para documentar que hace este modulo py

from pathlib import Path

path_archivo = Path("os.md")

print(path_archivo.exists())
print(path_archivo.name)
"""
True
os.md
"""

print("\n")

path_carpeta = Path("carpeta-fake")
print(path_carpeta.exists())
print(path_carpeta.name)
"""
True
carpeta-fake
"""

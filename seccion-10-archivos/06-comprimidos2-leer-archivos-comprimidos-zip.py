# ref. v104

from pathlib import Path
from zipfile import ZipFile
import os
os.system('cls' if os.name == 'nt' else 'clear')

# ejemplo de como leer un archivo comprimido ...
with ZipFile("seccion-10-archivos/comprimidos.zip") as zip:

    # obtengo los paths relativos de todos los archivos dentro del archivo comprimido
    # print(zip.namelist())

    # objeto con todo lo relacionado al archivo "seccion-10-archivos/06-comprimidos2-leer-archivos-comprimidos-zip.py", ubicado dentro del archivo comprimido
    info = zip.getinfo(
        "seccion-10-archivos/06-comprimidos2-leer-archivos-comprimidos-zip.py")
    print(info)

    # tamaño del archivo antes de la compresion, tamaño del archivo luego de la compresion
    print(info.file_size, info.compress_size)

    # extraer dentro de la carpeta "seccion-10-archivos/descomprimidos" todo el contenido del archivo comprimido "seccion-10-archivos/comprimidos.zip"
    zip.extractall("seccion-10-archivos/descomprimidos")

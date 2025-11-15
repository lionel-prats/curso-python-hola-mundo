# ref. v104

from pathlib import Path
from zipfile import ZipFile
import os
os.system('cls' if os.name == 'nt' else 'clear')

# ejemplo de como leer un archivo comprimido ...
with ZipFile(r"seccion-10-archivos\comprimidos.zip") as zip:

    # para ver todo lo que se encuentra dentro del archivo comprimido
    print(zip.namelist())

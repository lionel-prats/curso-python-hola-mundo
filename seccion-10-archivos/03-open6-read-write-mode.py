# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

with open("seccion-10-archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    print(texto)

    archivo.seek(0)

    texto[2] = "Chanchito feliz\n"
    print(texto)

    archivo.writelines(texto)

# seguir viendfo el v102

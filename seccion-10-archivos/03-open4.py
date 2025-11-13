# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

# with cierra en automatico los archivos que abrimos
with open("seccion-10-archivos/hola-mundo.txt", "r") as archivo:
    # el magic method __enter__ se va a ejecutar cuando hayamos abierto el archivo
    # el magic method __exit__ se va a ejecutar cuando se haya terminado de ejecutar todo lo que se encuentra dentro del bloque de with, y dentro del magic method __exit__ se esta cerrando el archivo de manera automatica

    print(archivo.readlines())

    archivo.seek(0)

    for linea in archivo:
        print(linea)

    # archivo.__enter__

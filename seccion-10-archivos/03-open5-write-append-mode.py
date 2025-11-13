# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

with open("seccion-10-archivos/hola-mundo.txt", "a+") as archivo:
    archivo.write('Chao mundo :(')

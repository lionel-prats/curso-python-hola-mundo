# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

archivo = open("seccion-10-archivos/hola-mundo.txt", "r")
texto = archivo.read()
print(texto)
archivo.close()

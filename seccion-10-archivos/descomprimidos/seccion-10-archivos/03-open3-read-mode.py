# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

# parametro "r" == read
# archivo = open("seccion-10-archivos/hola-mundo.txt", "r")
archivo = open("seccion-10-archivos/archivo-prueba.txt", "r")
texto = archivo.readlines()
print(texto)
archivo.close()

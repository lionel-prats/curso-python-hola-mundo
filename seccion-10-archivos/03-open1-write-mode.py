# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

# escritura
texto = "Hola mundo2!"

# me posiciono en el archivo, y si este no existe, lo crea
archivo = open("seccion-10-archivos/hola-mundo.txt", "w")

# reescribo el contenido
archivo.write(texto)

# siempre cerrar el archivo
archivo.close()

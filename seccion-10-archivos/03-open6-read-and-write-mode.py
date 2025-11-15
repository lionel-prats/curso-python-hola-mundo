# ref. v101

# from pprint import pprint
from io import open
import os
os.system('cls' if os.name == 'nt' else 'clear')

# parametro "r+" == lectura y escritura (...)
with open("seccion-10-archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    print(texto)

    archivo.seek(0)

    texto[0] = "Chanchito feliz1\n"
    texto[1] = "Chanchito feliz2\n"
    texto[2] = "Chanchito feliz3\n"
    print(texto)

    # el metodo writelines() nos permite escribir una lista dentro de nuestro archivo
    archivo.writelines(texto)

    # fake = ["1\n", "2\n", "3\n"]
    # archivo.writelines(fake)

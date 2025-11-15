# ref. v102

# from pprint import pprint
import csv
import os
os.system('cls' if os.name == 'nt' else 'clear')

with open("seccion-10-archivos/usuarios_gestion.csv", "r") as archivo:
    reader = csv.reader(archivo)  # instancia csv class

    print(reader)
    print(list(reader))

    archivo.seek(0)

    for linea in reader:
        print(linea)

from io import open

archivo = open("seccion-10-archivos/hola-mundo.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()

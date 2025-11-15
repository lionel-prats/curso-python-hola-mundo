# ref. v102

# from pprint import pprint
import csv
import os
os.system('cls' if os.name == 'nt' else 'clear')

# si no existe el archivo, se crea
# con el tercer parametro newline="" evito saltos de lineas no deseados
# en el csv a crear
with open("seccion-10-archivos/usuarios_gestion.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)  # instancia csv class
    writer.writerow(["userId", "email", "roleId"])
    writer.writerow(["266", "acasas@cecaitra.org.ar", "203"])
    writer.writerow(["292", "lprats@cecaitra.org.ar", "99"])
    writer.writerow(["317", "vjaime@cecaitra.org.ar", "20"])
    writer.writerow(["1042", "abruno@tandil.ar", "902"])
    # writer.writerows()

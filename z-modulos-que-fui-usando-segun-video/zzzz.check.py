import csv
import os

# 'as r' -> este lo vamos a utilizar como lectura
# 'as w' -> este lo vamos a u utilizar como un archivo temporal donde nosotros vamos a modificar lo que necesitemos
with open("seccion-10-archivos/usuarios_gestion.csv", "r") as r, open("seccion-10-archivos/usuarios_gestion_temp.csv", "w", newline="") as w:
    reader = csv.reader(r)  # instancia csv class
    writer = csv.writer(w)  # instancia csv class

    for linea in reader:
        userId = linea[0]
        if userId == "317":
            writer.writerow(["317", "vjaime@cecaitra.org.ar", "99"])
        else:
            writer.writerow(linea)

# elimino el archivo original
os.remove("seccion-10-archivos/usuarios_gestion.csv")

# renombro al archivo temp con el contenido actualizado, con el nombre del archivo original
os.rename(
    "seccion-10-archivos/usuarios_gestion_temp.csv",
    "seccion-10-archivos/usuarios_gestion.csv"
)

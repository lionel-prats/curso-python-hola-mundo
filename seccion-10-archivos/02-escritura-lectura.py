# ref. v100

from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

archivo = Path("seccion-10-archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
# print(type(texto))
# pprint(texto)

texto.insert(0, "Hola mundo!")
archivo.write_text("\n".join(texto), "utf-8")

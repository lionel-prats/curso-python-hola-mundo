## `MODULO csv` (video 102)
### Para qué sirve
El módulo csv de Python proporciona una interfaz eficiente y estandarizada para leer, escribir y manipular archivos CSV (Comma-Separated Values), uno de los formatos más utilizados para el intercambio de datos entre sistemas, aplicaciones y hojas de cálculo.  
Este módulo permite:
- Leer archivos CSV en forma de listas, diccionarios o estructuras personalizadas.
- Escribir archivos CSV con control de separadores, saltos de línea, comillas, y codificación.
- Gestionar de manera segura operaciones de actualización mediante archivos temporales.
- Asegurar compatibilidad con estándares como RFC 4180.
- Facilitar la importación y exportación de datos hacia/desde sistemas como Excel, bases de datos, APIs o scripts automatizados.

El módulo implementa clases como:
- csv.reader – interpreta un archivo CSV línea por línea y devuelve listas con los campos.
- csv.writer – escribe filas en un archivo CSV respetando delimitadores y formateos.
- csv.DictReader / csv.DictWriter – representan cada fila como diccionarios, ideal para columnas con encabezados.

Su principal ventaja es que abstrae toda la complejidad relacionada con:
- Gestión de delimitadores (, ; | etc.)
- Comillas y caracteres especiales
- Saltos de líneas entre sistemas (Windows, Linux, macOS)
- Archivos muy grandes que deben procesarse fila por fila

Esto convierte al módulo csv en una herramienta fundamental para trabajar con datasets livianos, registros de usuarios, logs, exportaciones de bases de datos y cualquier tipo de archivo tabular.

### Ejemplo de como crear un archivo csv (o reescribirlo si ya existe)
```python
import csv

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
```

### Ejemplo de como leer un archivo csv
```python
import csv

with open("seccion-10-archivos/usuarios_gestion.csv", "r") as archivo:
    reader = csv.reader(archivo)  # instancia csv class

    print(reader)
    print(list(reader))

    archivo.seek(0)

    for linea in reader:
        print(linea)

"""
<_csv.reader object at 0x0000021ADF7EE260>
[['userId', 'email', 'roleId'], ['266', 'acasas@cecaitra.org.ar', '203'], ['292', 'lprats@cecaitra.org.ar', '99'], ['317', 'vjaime@cecaitra.org.ar', '20'], ['1042', 'abruno@tandil.ar', '902']]
['userId', 'email', 'roleId']
['266', 'acasas@cecaitra.org.ar', '203']
['292', 'lprats@cecaitra.org.ar', '99']
['317', 'vjaime@cecaitra.org.ar', '20']
['1042', 'abruno@tandil.ar', '902']
"""
```

### Ejemplo de como modificar un archivo csv
```python
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
```
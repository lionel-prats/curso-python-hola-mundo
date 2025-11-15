# ref. v104

from pathlib import Path
from zipfile import ZipFile
import os
os.system('cls' if os.name == 'nt' else 'clear')

# ejemplo de como zipear toda la carpeta '/curso-python-holamundo'
with ZipFile("seccion-10-archivos/comprimidos.zip", "w") as zip:

    # con Path.rglob("*.*") indico que quiero que incluir dentro del archivo zip a crear todo el contenido de '/curso-python-holamundo'
    for path in Path().rglob("*.*"):

        # print(path)

        # me aseguro de no incluir en el zip a crear la referencia comprimidos.zip, el zip que va a contener todo '/curso-python-holamundo' comprimida
        # esta validacion es importante, ya que de lo contrario la ejecucion de este script entraria en un loop infinito
        if str(path) != r"seccion-10-archivos\comprimidos.zip":
            zip.write(path)
        else:
            print(path)
            print(type(path))
            print(str(path))
            print(type(str(path)))

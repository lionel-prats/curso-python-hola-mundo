# ref. v97/v98
# para ejecutar correctamente este script abrir la carpeta 'seccion-9-rutas' en una instancia nueva de VSCode

from pathlib import Path

path = Path()  # directorio actual, <class 'pathlib.WindowsPath'>

paths = [p for p in path.iterdir() if p.is_dir()]
# [WindowsPath('one'), WindowsPath('two')]

dependencias = {
    "db": "base de datos",
    "api": "esto es la api",
    "graphql": "esto es graphql"
}


def load(p):

    paquete = __import__(str(p).replace("/", "."))
    # la funcion __import__ se utiliza para importar paquetes y modeulos de manera dinamica

    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene funcion init")


list(map(load, paths))
# porque esto imprime lo siguiente en la terminal vvv

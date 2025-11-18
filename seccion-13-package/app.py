# ref. v123/v124

# crear un ambiente virtual (Windows) -> python -m venv env
# crear un ambiente virtual (Linux/MAC) -> python3 -m venv env

# activar el entorno virtual (Windows, cmd) -> env\Scripts\activate.bat
# activar el entorno virtual (Windows, powershell) -> .\env\Scripts\Activate.ps1
# activar el entorno virtual (Linux/MAC) -> source env/bin/activate

# desactivar el entorno virtual (Windows/Linux/MAC) -> deactivate

# comando para matar todos los procesos de Python en Windows -> taskkill /F /IM python.exe

# -------------------------------------------------------------------------------

# ref v125

# pip install pipenv -> instalacion de pipenv de manera global, en mi instalación global de Python
# -> con pipenv voy a a poder manejar el entorno virtual y las dependencias de cada app de manera mas moderna que con pip y venv

# pipenv install requests 
# -> instalo requests como libreria dentro del entorno virtual de la app 
# -> este comando creo los archivos Pipfile y Pipfile.lock

# pipenv --venv 
# -> para visualizar donde pipenv creo la carpeta que contiene nuestro ambiente virtual (fuera del proyecto)
# -> se creo en C:\Users\User\.virtualenvs\seccion-13-package-aUASrFo9

# pipenv shell 
# -> con este comando activamos el ambiente virtual de pipenv
# -> este comando lanza el ambiente virtual dentro de nuestra terminal

# exit 
# -> con este comando desactivamos el ambiente virtual de pipenv

# -------------------------------------------------------------------------------

# ref v126

# SIMULACION de como instalarme todas las dependencias del proyecto si solo tengo el Pipfile y el Pipfile.lock vvv 

# 1. localizo la carpeta del entorno virtual para borrarla y simular que recien me 'clono' el proyecto
# pipenv --venv
# C:\Users\User\.virtualenvs\seccion-13-package-aUASrFo9

# 2. abriente una terminal de bash en C:\Users\User\.virtualenvs, borro la carpeta del entorno virtual vvv
# rm -rf seccion-13-package-aUASrFo9/

# 3. regenero la carpeta del entorno virtual
# pipenv install

# 4. alternativa para regenerar la carpeta del entorno virtual, ignorando el Pipfile, y levantando la info del Pipfile.lock 
# pipenv install --ignore-pipfile
# esto es util para evitar conflicto de versiones en las dependencias (repasar ejemplo con la dependencia requests en el v126)

# -------------------------------------------------------------------------------

# ref. v127

# DEMO de gestion de dependencias 

# 1. para ver todas las dependencias, subdependencias, etc, instaladas dentro de nuestro proyecto vvv
# pipenv graph

# 2. desinstalo requests vvv
# pipenv uninstall requests
# comprobamos que el Pipfile y el Pipfile.lock se actualizaron correctamente
# pero, con 'pipenv graph' comprobamos que las subdependencias de requests siguen instaladas 

# 4. instalo la version 2.10 mas alta de requests vvv
# pipenv install requests==2.10.*

# 5. visaulizar por consola las dependencias que tienen versiones mas nuevas disponibles
# pipenv update --outdated

# 6. corrijo el Pipfile (ver video)

# 7. actualizo la dependencia requests
# pipenv update requests 
# este comando me permite actualizar todas las dependencias o la/s que yo quiera

# -------------------------------------------------------------------------------

# ref. v128




# -------------------------------------------------------------------------------

import requests
import json
import os

nombre_imagen = "NE_03521%2020250618002144.jpg"
endpoint = f"https://factory.cecaitra.ar/api/protocolos/326307/registros/por-imagen1/{nombre_imagen}"

r = requests.get(endpoint)
data = r.json()  # convierte automáticamente a dict

# os.system("cls" if os.name == "nt" else "clear")

print(json.dumps(data["data"]["lugar"], indent=4))


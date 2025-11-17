# ref. v123

# crear un ambiente virtual (Windows) -> python -m venv env
# crear un ambiente virtual (Linux/MAC) -> python3 -m venv env

# activar el entorno virtual (Windows) -> env\Scripts\activate.bat
# activar el entorno virtual (Linux/MAC) -> source env/bin/activate

# desactivar el entorno virtual (Windows/Linux/MAC) -> deactivate

import requests
import json
import os

nombre_imagen = "NE_03521%2020250618002144.jpg"
endpoint = f"https://factory.cecaitra.ar/api/protocolos/326307/registros/por-imagen1/{nombre_imagen}"

r = requests.get(endpoint)
data = r.json()   # convierte automáticamente a dict

os.system('cls' if os.name == 'nt' else 'clear')

print(json.dumps(data, indent=4))

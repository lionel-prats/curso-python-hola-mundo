# ref. v103

# from pprint import pprint
import json
from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

municipios = [
    {"id": "7", "descrip": "CABA"},
    {"id": "12", "descrip": "Tígre"},
    {"id": "165", "descrip": "Salta"},
]
print(municipios)
print(type(municipios))
print("\n")

# transformo la lista de diccionarios en un JSON con la libreria json
data = json.dumps(municipios, indent=4, ensure_ascii=False)
print(data)
print(type(data))

Path("seccion-10-archivos/municipios.json").write_text(data, encoding="utf-8")

# ref. v103

# from pprint import pprint
import json
from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

data = Path("seccion-10-archivos/municipios.json").read_text(encoding="utf-8")

municipios = json.loads(data)

for municipio in municipios:
    if municipio["id"] == "12":
        municipio["descrip"] = "Tígre RN"

Path("seccion-10-archivos/municipios.json").write_text(json.dumps(municipios,
                                                                  indent=4, ensure_ascii=False),
                                                       encoding="utf-8"
                                                       )

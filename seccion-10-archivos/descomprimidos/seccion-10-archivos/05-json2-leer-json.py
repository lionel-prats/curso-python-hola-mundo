# ref. v103

# from pprint import pprint
import json
from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

data = Path("seccion-10-archivos/municipios.json").read_text(encoding="utf-8")
print(data)
municipios = json.loads(data)
print(municipios)

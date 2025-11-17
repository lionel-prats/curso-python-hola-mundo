import json
from pathlib import Path

data = Path("seccion-10-archivos/municipios.json").read_text(encoding="utf-8")

municipios = json.loads(data)

for municipio in municipios:
    if municipio["id"] == "12":
        municipio["descrip"] = "Tígre RN"

Path("seccion-10-archivos/municipios.json").write_text(json.dumps(municipios,
                                                                  indent=4, ensure_ascii=False),
                                                       encoding="utf-8"
                                                       )


"""
El módulo json en Python se utiliza para convertir estructuras de datos de Python a JSON y viceversa, permitiendo intercambiar 
información entre aplicaciones, APIs, archivos y servicios externos.    
En resumen: te permite obtener un JSON prolijo, legible y válido a partir de tus datos de Python.
"""

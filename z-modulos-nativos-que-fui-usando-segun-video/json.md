## `MODULO json` (video 103)
### Para qué sirve
El módulo json de Python proporciona herramientas para serializar y deserializar datos en formato JSON (JavaScript Object Notation), el estándar más utilizado para el intercambio de información entre aplicaciones web, APIs, bases de datos, microservicios y sistemas distribuidos.

Este módulo permite:

- Convertir estructuras de Python (diccionarios, listas, números, strings, booleanos, None) a JSON mediante json.dumps().
- Interpretar JSON y convertirlo a tipos nativos de Python mediante json.loads().
- Leer y escribir archivos .json de manera segura, soportando Unicode, acentos, emojis y caracteres especiales.
- Mantener datos en un formato interoperable, legible y ampliamente compatible con sistemas modernos (JavaScript, Node.js, Java, PHP, Go, etc.).
- Formatear la salida con opciones como:
    - indent → sangría para mejor visualización,
    - ensure_ascii=False → mantener caracteres latinos tal cual,
    - sort_keys=True → ordenar claves alfabéticamente.

En la práctica, el módulo json es indispensable para:
- Persistir configuraciones, catálogos y estructuras livianas.
- Crear y consumir servicios REST.
- Exportar e importar datos entre sistemas.
- Almacenar información estructurada sin depender de bases de datos completas.
- Depurar estructuras complejas de manera clara y legible.

### Ejemplo de como crear un archivo json
```python
import json
from pathlib import Path

municipios = [
    {"id": "7", "descrip": "CABA"},
    {"id": "12", "descrip": "Tígre"},
    {"id": "165", "descrip": "Salta"},
]

# transformo la lista de diccionarios en un JSON con la libreria json
data = json.dumps(municipios, indent=4, ensure_ascii=False)
print(data)
print(type(data))

Path("seccion-10-archivos/municipios.json").write_text(data, encoding="utf-8")

"""
[
    {
        "id": "7",
        "descrip": "CABA"
    },
    {
        "id": "12",
        "descrip": "Tígre"
    },
    {
        "id": "165",
        "descrip": "Salta"
    }
]
<class 'str'>
"""
```

### Ejemplo de como leer un archivo json
```python
import json
from pathlib import Path

data = Path("seccion-10-archivos/municipios.json").read_text(encoding="utf-8")
print(data)
municipios = json.loads(data)
print(municipios)

"""
[
    {
        "id": "7",
        "descrip": "CABA"
    },
    {
        "id": "12",
        "descrip": "Tígre"
    },
    {
        "id": "165",
        "descrip": "Salta"
    }
]
<class 'str'>
[{'id': '7', 'descrip': 'CABA'}, {'id': '12', 'descrip': 'Tígre'}, {'id': '165', 'descrip': 'Salta'}]
<class 'list'>
"""
```

### Ejemplo de como modificar un archivo json
```python
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
```

### Ejemplo de uso como helper
En el siguiente ejemplo usamos json.dumps() para serializar (convertir) un diccionario o lista de Python en una cadena JSON legible y estandarizada, agregando sangría (indent) para mejorar la claridad visual.   
Esto resulta ideal cuando se quiere:

- guardar datos en archivos .json,
- imprimir resultados con formato limpio,
- preparar estructuras para ser enviadas a APIs REST,
- documentar o depurar información de manera clara.
```python
import json

diccionario_py = {"id": 7, "nombre": "CABA", "poblacion": 3000000}

print(json.dumps(diccionario_py, indent=4))
"""
{
    "id": 7,
    "nombre": "CABA",
    "poblacion": 3000000
}
"""
```
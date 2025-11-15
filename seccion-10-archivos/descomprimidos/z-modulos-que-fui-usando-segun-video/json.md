## `json` (video 103)
### Para qué sirve

El módulo json en Python se utiliza para convertir estructuras de datos de Python a JSON y viceversa, permitiendo intercambiar 
información entre aplicaciones, APIs, archivos y servicios externos.    
En resumen: te permite obtener un JSON prolijo, legible y válido a partir de tus datos de Python.

### Ejemplo1
```python
# ...
```

En el siguiente ejemplo usamos json.dumps() para serializar (convertir) un diccionario o lista de Python en una cadena JSON legible y estandarizada, agregando sangría (indent) para mejorar la claridad visual.   
Esto resulta ideal cuando se quiere:

- guardar datos en archivos .json,
- imprimir resultados con formato limpio,
- preparar estructuras para ser enviadas a APIs REST,
- documentar o depurar información de manera clara.
### Ejemplo2
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
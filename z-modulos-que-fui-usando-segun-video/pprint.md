## `pprint` (video 62)
### Para qué sirve

El módulo `pprint` ("pretty print") proporciona funciones para **imprimir estructuras de datos complejas de forma legible y visualmente organizada**.  
Es especialmente útil cuando se trabaja con:

- Listas anidadas  
- Diccionarios con muchos elementos  
- Datos JSON convertidos a estructuras Python  
- Respuestas de APIs  
- Cualquier objeto cuya visualización estándar resulte difícil de leer

`pprint` formatea la salida aplicando sangrías, saltos de línea, alineación y espaciado adecuado, lo que facilita la depuración, el análisis y la comprensión de la información.  
Además, permite ajustar parámetros como `indent`, `width` y `depth` para controlar la forma exacta del formateo.

En síntesis, `pprint` es una herramienta ideal para **depurar**, **inspeccionar** y **presentar** datos complejos de manera clara y ordenada en la terminal.

### Ejemplo
```python
from pprint import pprint

pprint(
    {"id": 7, "nombre": "CABA", "poblacion": 3000000},
    indent=4,
    width=1,
)
# salida mas aproximada a la desada usando pprint vvv
"""
{   'id': 7,
    'nombre': 'CABA',
    'poblacion': 3000000}
"""
# hay una opcion mas PRO usando la libreria json (ver json.md)
```
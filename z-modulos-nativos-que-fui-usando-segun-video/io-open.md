## `MODULO io - funcion open` (video 101)
### Para qué sirve
El módulo io de Python proporciona una interfaz uniforme para manejar flujos de entrada y salida, permitiendo trabajar con archivos, buffers en memoria, streams binarios y streams de texto de manera consistente y eficiente.  
Aunque Python expone la función integrada open() de forma directa, esta función en realidad es un wrapper que utiliza las clases internas del módulo io, por lo que io es la base del sistema completo de I/O de Python.  
La función open() es el mecanismo estándar para:
- Abrir archivos en distintos modos: lectura, escritura, append, actualización.
- Leer y escribir contenido en formato texto o binario.
- Gestionar la codificación de caracteres (UTF-8, ASCII, etc.).
- Trabajar con archivos de forma segura mediante context managers (with), evitando fugas de recursos.
- Obtener un objeto archivo, que implementa métodos como .read(), .readline(), .write(), .close(), etc.

En resumen, open() es la puerta de entrada para cualquier operación de lectura/escritura de archivos, respaldada por las clases del módulo io que garantizan un comportamiento consistente, seguro y optimizado.

### Ejemplo lectura archivo sin with
```python
from io import open

archivo = open("seccion-10-archivos/hola-mundo.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()

"""
Hola mundo1!

Hola mundo2!

Hola mundo3!
"""
```

### Ejemplo lectura archivo con with
```python
from io import open

with open("seccion-10-archivos/hola-mundo.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

"""
Hola mundo1!

Hola mundo2!

Hola mundo3!
"""
```

### Ver más ejemplos de escritura, modificación, etc. en los archivos del v101.
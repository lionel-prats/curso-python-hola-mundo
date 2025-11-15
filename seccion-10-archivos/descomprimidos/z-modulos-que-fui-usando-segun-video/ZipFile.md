## `ZipFile` (video 104)
### Para qué sirve
El módulo zipfile de Python proporciona herramientas para crear, leer, modificar y extraer archivos ZIP directamente desde código, sin depender de aplicaciones externas.  
ZipFile permite:
- Comprimir archivos y carpetas completas en un único archivo .zip.
- Agregar o remover elementos dentro de un ZIP existente.
- Listar y explorar el contenido de un archivo ZIP sin necesidad de descomprimirlo completamente.
- Extraer archivos individuales o el contenido completo del ZIP a una ubicación específica.
- Este módulo es especialmente útil para automatizar backups, empaquetar proyectos, distribuir archivos, generar exportaciones comprimidas o procesar archivos ZIP generados por otros sistemas.
- Además, su API es simple y segura, permitiendo trabajar con rutas, filtros y compresión de forma controlada y programática.

### Ejemplo de como zipear toda la carpeta '/curso-python-holamundo'
```python
from pathlib import Path
from zipfile import ZipFile

# ejemplo de como zipear toda la carpeta '/curso-python-holamundo'
with ZipFile("seccion-10-archivos/comprimidos.zip", "w") as zip:

    # con Path.rglob("*.*") indico que quiero que incluir dentro del zip a crear todo el contenido de '/curso-python-holamundo'
    for path in Path().rglob("*.*"):

        # print(path)

        # me aseguro de no incluir en el zip a crear la referencia comprimidos.zip, el zip que va a contener todo '/curso-python-holamundo' comprimida
        # esta validacion es importante, ya que de lo contrario la ejecucion de este script entraria en un loop infinito
        if str(path) != r"seccion-10-archivos\comprimidos.zip":
            zip.write(path)
        else:
            print(path)
            print(type(path))
            print(str(path))
            print(type(str(path)))
```
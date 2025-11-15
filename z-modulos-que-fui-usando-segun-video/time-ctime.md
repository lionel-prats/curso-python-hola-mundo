## `MODULO time - funcion ctime` (video 99)
### Para qué sirve
La función ctime() forma parte del módulo estándar time de Python y se utiliza para convertir un valor de tiempo expresado en segundos desde la época UNIX (epoch) en una cadena de texto legible para humanos.  
Su propósito principal es transformar valores numéricos de marcas de tiempo—como los obtenidos mediante `stat

### Ejemplo
```python
from pathlib import Path
from time import ctime

archivo = Path("z-modulos-que-fui-usando-segun-video/os.md")

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
"""
acceso Sat Nov 15 16:40:39 2025
creacion Sat Nov 15 12:59:18 2025
modificacion Sat Nov 15 15:20:49 2025
"""
```
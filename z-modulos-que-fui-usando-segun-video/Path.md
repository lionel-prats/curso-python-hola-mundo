## `Path` (video 95)
### Para qué sirve

La clase `Path`, del módulo `pathlib`, proporciona una forma **moderna, orientada a objetos y multiplataforma** de trabajar con rutas de archivos y directorios.  
Reemplaza al uso tradicional de `os.path`, ofreciendo una sintaxis más clara, expresiva y segura.

Permite:

- Construir rutas absolutas o relativas de manera sencilla.
- Navegar y manipular rutas como si fueran objetos (concatenación, padres, nombres, extensiones).
- Comprobar existencia, tipo y propiedades de archivos o carpetas.
- Leer y escribir contenido directamente (`read_text()`, `write_text()`, etc.).
- Crear carpetas, eliminar archivos, recorrer directorios.
- Garantizar compatibilidad automática entre Windows, Linux y macOS.

En resumen, `Path` facilita trabajar con el sistema de archivos de forma intuitiva, limpia y robusta, reduciendo errores y mejorando la mantenibilidad del código.

### Ejemplo
```python
from pathlib import Path

path_archivo = Path("os.md")

print(path_archivo.exists())
print(path_archivo.name)
"""
True
os.md
"""

print("\n")

path_carpeta = Path("carpeta-fake")
print(path_carpeta.exists())
print(path_carpeta.name)
"""
True
carpeta-fake
"""
```
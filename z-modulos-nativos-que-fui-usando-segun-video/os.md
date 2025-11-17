## `os` (video 102)
### Para qué sirve
El módulo os proporciona una interfaz para interactuar con el sistema operativo desde Python.  
Permite ejecutar tareas esenciales relacionadas con el entorno del sistema, como:
- Gestionar archivos y directorios (crear, eliminar, renombrar, mover).
- Consultar información del sistema (tipo de SO, variables de entorno, rutas, permisos).
- Ejecutar comandos externos del sistema operativo.
- Trabajar con rutas, procesos y recursos del sistema.
- Es una capa de abstracción que permite que tu código funcione tanto en Windows, macOS como Linux, sin necesidad de modificarlo para cada plataforma.
- En este curso, su uso se centra especialmente en:
- Limpieza de consola como truco visual durante pruebas.
- Eliminación y renombrado de archivos para manipular datos almacenados en disco.

### Ejemplo de uso limpiar consola (truco mío)
```python
import os

os.system('cls' if os.name == 'nt' else 'clear')
```

### Ejemplo de uso eliminar y/o renombrar archivos (video 102)
```python
import os

# elimino el archivo original
os.remove("seccion-10-archivos/usuarios_gestion.csv")

# renombro al archivo temp con el contenido actualizado, con el nombre del archivo original
os.rename(
    "seccion-10-archivos/usuarios_gestion_temp.csv",
    "seccion-10-archivos/usuarios_gestion.csv"
)
```
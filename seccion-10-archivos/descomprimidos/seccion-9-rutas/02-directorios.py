# ref. v96

from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

# path = Path(r"seccion-9-rutas")
path = Path("seccion-9-rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

for p in path.iterdir():
    print(p)

# utilizo la comprension de listas
solo_archivos = [p for p in path.iterdir() if not p.is_dir()]
print(solo_archivos)

# utilizo la comprension de listas
solo_archivos_clase2 = [p for p in path.glob("02*.py")]
print(solo_archivos_clase2)

# path.glob("**/*.py" === path.rglob("*.py"
solo_archivos_py_recursivamente = [p for p in path.glob("**/*.py")]
solo_archivos_py_recursivamente = [p for p in path.rglob("*.py")]
print(solo_archivos_py_recursivamente)

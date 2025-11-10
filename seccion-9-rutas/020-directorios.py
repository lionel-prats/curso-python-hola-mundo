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

solo_archivos = [p for p in path.iterdir() if not p.is_dir()]
print(solo_archivos)

solo_archivos_clase2 = [p for p in path.glob("020*.py")]
print(solo_archivos_clase2)

# v 96 no terminado, reveerlo desde cero.

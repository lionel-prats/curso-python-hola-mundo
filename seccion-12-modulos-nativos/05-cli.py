# ref. v118

import sys
from pathlib import Path
import os


def cli(args):

    # python seccion-12-modulos-nativos/05-cli.py
    if len(args) == 1:
        print("no se pasaro argumentos")
        return

    # python seccion-12-modulos-nativos/05-cli.py seccion-12-modulos-nativos/lalaxxx
    if len(args) != 3:
        print("se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)

    # python seccion-12-modulos-nativos/05-cli.py seccion-12-modulos-nativos/lalaxxx seccion-12-modulos-nativos/moco.md
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)

    # python seccion-12-modulos-nativos/05-cli.py seccion-12-modulos-nativos/lala seccion-12-modulos-nativos/moco.md
    if d.exists():
        print("el destino no puede existir")
        return

    # python seccion-12-modulos-nativos/05-cli.py seccion-12-modulos-nativos/lala seccion-12-modulos-nativos/lala-destino.md
    os.rename(str(origen), str(destino))
    print("archivo renombrado con exito")


os.system('cls' if os.name == 'nt' else 'clear')
cli(sys.argv)

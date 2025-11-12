# ref. v99

from pathlib import Path
from time import ctime
import os
os.system('cls' if os.name == 'nt' else 'clear')

archivo = Path("seccion-10-archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# estadisticas del archivo
# print(archivo.stat()) #
# os.stat_result(st_mode=33206, st_ino=10696049115788833, st_dev=7947206455523143695, st_nlink=1, st_uid=0, st_gid=0, st_size=1375, st_atime=1762904994, st_mtime=1762904994, st_ctime=1762904819)

# fecha de acceso al archivo
print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))

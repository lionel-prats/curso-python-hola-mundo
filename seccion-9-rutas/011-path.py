# ref. v95


from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

path1 = Path("hola-mundo/mi-archivo.py")
print(path1.is_file())
print(path1.is_dir())
print(path1.exists())
print(path1.name)
print(path1.stem)
print(path1.suffix)
print(path1.parent)
print(path1.absolute())

print("\n")

path2 = Path(r"hola-mundo\mi-archivo.py")
print(path2.is_file())
print(path2.is_dir())
print(path2.exists())
print(path2.name)
print(path2.stem)
print(path2.suffix)
print(path2.parent)
print(path2.absolute())

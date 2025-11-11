# ref. v95

from pathlib import Path
import os
os.system('cls' if os.name == 'nt' else 'clear')

path = Path(r"hola-mundo\mi-archivo.py")
p = path.with_name("chanchito.exe")

print(type(path))
print(path.absolute())

print("\n")

print(type(p))
print(p.absolute())

print("\n")

p = path.with_suffix(".bat")

print(type(p))
print(p.absolute())

p = path.with_stem("feliz")

print("\n")

print(type(p))
print(p.absolute())

import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 65


class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)

print(mi_perro)
# <__main__.Perro object at 0x00000 1EE85529DF 0> # ejecucion 1
# <__main__.Perro object at 0x00000 22F5B729B2 0> # ejecucion 2
# <__main__.Perro object at 0x00000 20B17FA9B2 0> # ejecucion 3
# <__main__.Perro object at 0x00000 22C4A619B2 0> # ejecucion 4
# <__main__.Perro object at 0x00000 2E5939C9B2 0> # ejecucion 5
# <__main__.Perro object at 0x00000 15F906F9B2 0> # ejecucion 6
# <__main__.Perro object at 0x00000 2AADE8FA09 0> # ejecucion 7

print(mi_perro.nombre)

mi_perro2 = Perro("Felipe", 3)
print(mi_perro)   # <__main__.Perro object at 0x00000 2AADE8FA09 0> # ejecucion 7
print(mi_perro2)  # <__main__.Perro object at 0x00000 2AADE8FA0F 0> # ejecucion 7
print(mi_perro2.nombre)

mi_perro.habla()
mi_perro2.habla()

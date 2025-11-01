import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 64


class Perro:
    def habla(self):
        print("Guau!")


mi_perro = Perro()
print(mi_perro)  # <__main__.Perro object at 0x0000019F7D529F40>

print(type("hola mundo"))
print(type(mi_perro))

mi_perro.habla()

print(isinstance(mi_perro, Perro))
print(isinstance("hola mundo", str))

# ref. v67

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Perro:
    patas = 4  # propiedad de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # def habla():
    #     print("Guau!")

    @classmethod  # esto es un decorador, indica que se trata de un metodo de clase
    def habla(cls):
        print("Guau!")

    @classmethod  # esto es un decorador, indica que se trata de un metodo de clase
    def factory(cls):
        return cls("Chanchito feliz", 4)


Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)

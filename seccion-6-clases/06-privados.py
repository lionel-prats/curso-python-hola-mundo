# ref. v68

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # propiedad/atributo privad@
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod  # esto es un decorador, indica que se trata de un metodo de clase
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro.factory()

perro1.habla()
# print(perro1.__nombre)
print(perro1.get_nombre())
print(perro1.__dict__)
print(perro1._Perro__nombre)

import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 69


class Perro:

    def __init__(self, nombre):
        self.nombre = nombre

    @property  # decorador property, tranforma al metodo de abajo en una property
    def nombre(self):  # getter -> metodo que nos devuelve un valor
        print("pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):  # setter -> metodo que se encarga de setear un valor
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
# perro = Perro(True)
print(perro.nombre)

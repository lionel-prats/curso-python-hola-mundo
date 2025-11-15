# ref. v74

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Chanchito(Perro):
    def programar(self):
        print("programando")


perro = Perro()
perro.pasear()

chanchito = Chanchito()
chanchito.comer()

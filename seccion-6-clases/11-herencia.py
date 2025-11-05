import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 74


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

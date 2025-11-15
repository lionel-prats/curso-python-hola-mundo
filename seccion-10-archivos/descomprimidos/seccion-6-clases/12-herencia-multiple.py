import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 75


class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro(Caminador, Nadador):
    pass


class Pinguino(Nadador, Volador):
    pass


class Paloma(Caminador, Volador):
    pass


class Pato(Caminador, Nadador, Volador):
    pass

import os
os.system('cls' if os.name == 'nt' else 'clear')
# ref. video 76

# ANULACION DE METODO == METHOD OVERRIDE


class Ave:
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):

    def __init__(self):

        # ejecuto el constructor de la clase padre para poder heredar el atributo volador
        super().__init__()

        self.nadador = "nadador"

    def vuela(self):
        # super().vuela() # puedo invocar a metodos heredados
        print("vuela pato")


pato = Pato()
pato.vuela()

print(pato.volador, pato.nadador)

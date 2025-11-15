# ref. v70

import os
os.system('cls' if os.name == 'nt' else 'clear')

# metodos magicos disponibles en Python vvv
# https://rszalski.github.io/magicmethods/


class Perro:

    # metodos magicos son metodos que se van a ejecutar cuando nosotros no los estemos llamando directamente
    # el constructor es un metodo magico
    def __init__(self, nombre, edad):
        print("pasando por constructor")
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print("Soy el metodo magico __del__, me ejecuto cuando alguna instancia de esta clase es eliminada de memoria")

    # salida customizada para brindar info de la clase
    def __str__(self):
        return f"Instancia de Equipo, serie = {self.nombre}, antiguedad = {self.edad}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Chanchito", 7)
del perro

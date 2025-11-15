# ref. v77

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en DDBB")

    @classmethod  # esto es un decorador, indica que se trata de un metodo de clase
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    # pass
    tabla = "Usuario"


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)

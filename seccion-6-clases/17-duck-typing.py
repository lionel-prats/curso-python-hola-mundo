# ref. v80

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Usuario():
    def guardar(self):
        print(f"Guardando en BBDD")


class Sesion():
    def guardar(self):
        print(f"Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])

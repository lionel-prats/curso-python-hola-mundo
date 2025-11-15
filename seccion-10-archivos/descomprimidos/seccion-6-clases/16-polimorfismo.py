# ref. video 79

from abc import ABC, abstractmethod
import os
os.system('cls' if os.name == 'nt' else 'clear')


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print(f"Guardando en BBDD")


# las sesiones son lo que le permiten a un servidor identificar cuando un usuario se esta conectando
# y tambien a quien pertenece cada una de las peticiones que el usuario esta realizando
# las sesiones por lo general se guardan en disco duro, en un archivo
class Sesion(Model):
    def guardar(self):
        print(f"Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])

# ref. video 78
from abc import ABC, abstractmethod

# ABC = Abstract Class -> es la clase de la cual tiene que heredar cualquier clase que querramos que sea abstracta
# abstractmethod = nos sirve para declarar atributos y metodos abstractos

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Model(ABC):

    # con esta propiedad abstracta definida, oblicamos a las clases que heredan de Model que tengan que necesariamente definir esta variable
    @property
    @abstractmethod
    def tabla(self):
        print("pasando por getter")

    @abstractmethod
    def guardar(self):
        pass

    @classmethod  # esto es un decorador, indica que se trata de un metodo de clase
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando {self.tabla} en DDBB")

# usuario = Model()
# Model.buscar_por_id(123)


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)

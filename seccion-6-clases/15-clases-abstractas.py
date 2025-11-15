# ref. v78

from abc import ABC, abstractmethod
# ABC = Abstract Base Classes (modulo py) -> es la clase de la cual tiene que heredar cualquier clase que querramos que sea abstracta
# abstractmethod = nos sirve para declarar atributos y metodos abstractos dentro de una clase abstracta,
# lo cual implica que cualquier clase que herede de una clase abstracta con propiedades y/o metodos abstractos,
# debe necesariamente declarar estas/os propiedades y/o metodos

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Model(ABC):
    """
    al heredar de la clase ABC (modulo default de py), ahora Model es una clase abstracta
    por ende, nos aseguramos que no se puedan generar instancias de la clase Model
    """

    # con esta propiedad abstracta definida, obligamos a las clases que heredan de Model a definir esta propiedad
    @property
    @abstractmethod
    def tabla(self):
        print("pasando por getter")

    # con este metodo abstracto definido, obligamos a las clases que heredan de Model a definir este metodo
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


# model = Model()
# Model.buscar_por_id(123)


usuario = Usuario()
usuario.guardar()
print(usuario.tabla)
Usuario.buscar_por_id(123)

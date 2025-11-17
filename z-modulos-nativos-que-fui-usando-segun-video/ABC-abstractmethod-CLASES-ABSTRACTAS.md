## `ABC, abstractmethod` (video 78)
### ¿Qué son ABC y abstractmethod y para qué sirven?
El módulo abc (Abstract Base Classes) de la biblioteca estándar de Python proporciona las herramientas necesarias para definir clases base abstractas, un mecanismo fundamental en la programación orientada a objetos cuando se busca establecer contratos formales entre clases.  
Una clase abstracta es una clase que no puede ser instanciada directamente y que define una estructura común para sus subclases.  
Esto permite asegurar que todas las clases que hereden de ella implementen ciertos métodos o propiedades indispensables para el correcto funcionamiento del sistema.  

Los dos elementos principales del módulo son:

- ABC
Es una clase base que permite marcar una clase como abstracta. Al heredar de ABC, una clase puede declarar métodos abstractos y evitar que sea instanciada hasta que todas sus abstracciones sean implementadas por sus subclases.
- @abstractmethod
Es un decorador utilizado para declarar métodos (o propiedades) abstractos dentro de una clase abstracta.  
Cualquier clase que herede de esa base está obligada a proporcionar una implementación concreta de dichos métodos; de lo contrario, también será considerada abstracta y no podrá instanciarse.

Este mecanismo es especialmente útil para:
- Definir interfaces o contratos formales que otras clases deben cumplir.
- Garantizar una estructura uniforme en jerarquías de clases complejas.
- Facilitar la extensibilidad y robustez del código.
- Evitar errores en tiempos de ejecución al asegurar que los métodos esenciales siempre estén implementados.

En resumen, ABC y abstractmethod permiten implementar un paradigma de diseño basado en contratos y garantizar que las clases derivadas respeten una API común, mejorando la mantenibilidad, claridad y consistencia del código orientado a objetos en Python.

### Ejemplo
```python
from abc import ABC, abstractmethod
# ABC = Abstract Base Classes (modulo py) -> es la clase de la cual tiene que heredar cualquier clase que querramos que sea abstracta
# abstractmethod = nos sirve para declarar atributos y metodos abstractos dentro de una clase abstracta,
# lo cual implica que cualquier clase que herede de una clase abstracta con propiedades y/o metodos abstractos,
# debe necesariamente declarar estas/os propiedades y/o metodos

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


usuario = Usuario()
usuario.guardar()
print(usuario.tabla)
Usuario.buscar_por_id(123)

"""
Guardando Usuario en DDBB
Usuario
Buscando por id 123 en la tabla Usuario
"""

```
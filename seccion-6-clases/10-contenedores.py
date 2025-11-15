# ref. v73

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    # productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.imprimir()
print("\n")
deportes.agregar(surfboard)
deportes.imprimir()

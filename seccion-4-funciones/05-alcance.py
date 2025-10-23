saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    # saludo = "Hola Chanchito"
    global saludo

    print(saludo)


print(saludo)
saludar()
saludaChanchito()

# seguir por el video 42 - Depurando funciones

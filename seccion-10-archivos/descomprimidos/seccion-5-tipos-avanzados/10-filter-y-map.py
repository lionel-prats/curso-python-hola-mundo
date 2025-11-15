import os
os.system('cls' if os.name == 'nt' else 'clear')

usuarios = [
    ("Chanchito", 4),
    ("Felipe", 1),
    ("Pulga", 5)
]
print(usuarios)

# transformacion
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# filtrado
usuarios_filtrados = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(usuarios_filtrados)

# filtrado y transformacion
usuarios_filtrados_transformados = list(
    map(lambda usuario: usuario[0], usuarios_filtrados))
print(usuarios_filtrados_transformados)

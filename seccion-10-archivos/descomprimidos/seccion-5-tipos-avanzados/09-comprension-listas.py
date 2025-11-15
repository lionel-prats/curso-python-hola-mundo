import os
os.system('cls' if os.name == 'nt' else 'clear')

usuarios = [
    ("Chanchito", 4),
    ("Felipe", 1),
    ("Pulga", 5)
]
print(usuarios)

# transformacion
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filtrado
usuarios_filtrados = [usuario for usuario in usuarios if usuario[1] > 2]
print(usuarios_filtrados)

# filtrado y transformacion
usuarios_filtrados_transformados = [usuario[0]
                                    for usuario in usuarios if usuario[1] > 2]
print(usuarios_filtrados_transformados)

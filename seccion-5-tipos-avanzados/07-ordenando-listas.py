import os
os.system('cls' if os.name == 'nt' else 'clear')

# numeros = [2, 4, 1, 45, 75, 22]
# numeros.sort()
# numeros.sort(reverse=True)
# numeros2 = sorted(numeros)
# numeros2 = sorted(numeros, reverse=True)
# print(numeros)
# print(numeros2)

usuarios = [
    (4, "Chanchito"),
    (1, "Felipe"),
    (5, "Pulga")
]
usuarios = [
    ("Wagner", "Tomás", 1),
    ("Prats", "Lionel", 4),
    ("Salgán", "Alejo", 5)
]


def ordenar_por_id(elemento):
    return elemento[2]


def ordenar_por_apellido(elemento):
    return elemento[0]


def ordenar_por_nombre(elemento):
    return elemento[1]


usuarios.sort(key=ordenar_por_id)
usuarios.sort(key=ordenar_por_id, reverse=True)
print(usuarios)
print("\n")

usuarios.sort(key=ordenar_por_nombre)
usuarios.sort(key=ordenar_por_nombre, reverse=True)
print(usuarios)
print("\n")

usuarios.sort(key=ordenar_por_apellido)
usuarios.sort(key=ordenar_por_apellido, reverse=True)
print(usuarios)
print("\n")

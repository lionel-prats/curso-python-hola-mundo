import os
os.system('cls' if os.name == 'nt' else 'clear')

mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")
print(mascotas)

mascotas.remove("Pulga")
mascotas.pop()
mascotas.pop(1)
del mascotas[0]
print(mascotas)

# mascotas = []
mascotas.clear()
print(mascotas)

# if "Felipe" in mascotas:
#     print(mascotas.index("Felipe"))

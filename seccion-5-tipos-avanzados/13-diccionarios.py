import os
os.system('cls' if os.name == 'nt' else 'clear')

punto = {"x": 25, "y": 50}
print(punto["x"])

punto["z"] = 45
print(punto)

if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("y", 844))
print(punto.get("lala", 97))


del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


print("\n")

usuarios = [
    {"id": 1, "nombre": "Lionel"},
    {"id": 2, "nombre": "Tomás"},
    {"id": 3, "nombre": "Luis"},
    {"id": 4, "nombre": "Alejo"}
]

for usuario in usuarios:
    print(usuario["nombre"])

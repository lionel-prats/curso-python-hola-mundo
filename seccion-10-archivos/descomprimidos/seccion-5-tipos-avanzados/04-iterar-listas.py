import os
os.system('cls' if os.name == 'nt' else 'clear')

mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

for mascota in (mascotas):
    print(mascota)
print("\n")

for mascota in enumerate(mascotas):
    print(mascota)
print("\n")

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)

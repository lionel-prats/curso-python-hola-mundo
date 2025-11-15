import os
os.system('cls' if os.name == 'nt' else 'clear')

mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz", "Felipe"]

print(mascotas.count("Felipe"))
if "Felipe" in mascotas:
    print(mascotas.index("Felipe"))

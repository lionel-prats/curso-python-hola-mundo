import os
os.system('cls' if os.name == 'nt' else 'clear')

usuarios = [
    ("Wagner", "Tomás", 1),
    ("Prats", "Lionel", 4),
    ("Salgán", "Alejo", 5)
]

# ORDENAR LISTADO DE USUARIOS POR ID ASC/DESC
# usuarios.sort(key=lambda el: el[2])
usuarios.sort(key=lambda el: el[2], reverse=True)
print(usuarios)
print("\n")


# ORDENAR LISTADO DE USUARIOS POR APELLIDO ASC/DESC
usuarios.sort(key=lambda el: el[0])
# usuarios.sort(key=lambda el: el[0], reverse=True)
print(usuarios)
print("\n")


# ORDENAR LISTADO DE USUARIOS POR NOMBRE ASC/DESC
usuarios.sort(key=lambda el: el[1])
# usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
print("\n")

import os
os.system('cls' if os.name == 'nt' else 'clear')

lista1 = [1, 2, 3, 4]
# lista1 = (1, 2, 3, 4)
# print(*lista1, "\n")

lista2 = [5, 6]

combinada = ["hola", *lista1, "mundo", *lista2, "chanchito"]
print(combinada, "\n")

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, "z": "mundo", **punto2}
print(nuevoPunto, "\n")
nuevoPunto = {**punto2, **punto1, "lala": "hola mundo"}
print(nuevoPunto, "\n")

import os
os.system('cls' if os.name == 'nt' else 'clear')


# numeros = [1, 2, 3]
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
# print(primero, segundo, tercero)
# print(numeros)
# primer_elemento, *resto_elementos = numeros
# print(primer_elemento, resto_elementos)

numeros2 = list(range(1, 10))
print(numeros2)
primero, segundo, *otros, penu, ultimo = numeros2
print(segundo, penu, otros)

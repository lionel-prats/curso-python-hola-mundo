# pilas o colas -> las pilas o colas en python cumplen con la caracteristica de ser LIFO -> Last In First Out

import os
os.system('cls' if os.name == 'nt' else 'clear')

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoElemento = pila.pop()
print(pila)
print(ultimoElemento)
print(pila[-1])

pila.pop()
pila.pop()
if not pila:
    print("pila vacia")

# set en ingles significa 'grupo' o 'conjunto'
# set en py es una coleccion de datos que no se puede repetir y que tampoco esta ordenada

import os
os.system('cls' if os.name == 'nt' else 'clear')

# primer = {1, 1, 2, 2, 3, 4}
primer = {2, 2, 1, 1, 3, 4}
# print(primer)
primer.add(5)
primer.remove(1)
print("set primer", primer)

segundo = [3, 6, 4, 5]
segundo = set(segundo)
print("set segundo", segundo)
print("union", primer | segundo)  # union
print("interseccion", primer & segundo)  # interseccion

# diferencia (retorna un set con los elementos de la izquierda, que no se encuentran en el elemento de la derecha)
print("diferencia primer", primer - segundo)

# diferencia (retorna un set con los elementos de la izquierda, que no se encuentran en el elemento de la derecha)
print("diferencia segundo", segundo - primer)

# diferencia simetrica (caracter 'caret' == ^ -> codigo ASCII == Alt+94) (retorna los elementos excluyentes de cada set)
print("diferencia simetrica", primer ^ segundo)

if 5 in segundo:
    print(f"el set {segundo} incluye el valor {5}")

print(list(primer ^ segundo))

# ref. v59

# filas -> las filas en python cumplen con la caracteristica de ser FIFO -> First In First Out

from collections import deque

import os
os.system('cls' if os.name == 'nt' else 'clear')

# deque() es una clase
# recibe como primer elemento un iterable
fila = deque([1, 2])

fila.append(3)
fila.append(4)
fila.append(5)
print(fila)

fila.popleft()
print(fila)

fila.popleft()
fila.popleft()
fila.popleft()
if not fila:
    print("fila vacia")
else:
    print("fila aun no esta vacia")

fila.popleft()

if not fila:
    print("fila vacia")
else:
    print("fila aun no esta vacia")

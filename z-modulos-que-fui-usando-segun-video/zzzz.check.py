from collections import deque

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

"""
deque([1, 2, 3, 4, 5])
deque([2, 3, 4, 5])
fila aun no esta vacia
fila vacia
"""

## `MODULO deque` (video 59)
### Para qué sirve
El tipo deque (double-ended queue) del módulo estándar collections proporciona una estructura de datos optimizada para inserciones y eliminaciones rápidas en ambos extremos.  
A diferencia de las listas nativas de Python, cuyos costos de inserción/eliminación al inicio son altos (O(n)), un deque ofrece operaciones append y pop a izquierda o derecha en tiempo constante O(1), incluso para grandes volúmenes de datos.  
Por este motivo, es ideal para implementar:
- Colas (queues)
- Pilas (stacks)
- Colas FIFO y LIFO eficientes
- Buffers deslizantes (sliding windows)
- Procesamientos secuenciales donde se agregan y consumen elementos de manera simultánea
- Algoritmos que requieren acceso eficiente a ambos extremos de la estructura

Además, deque incluye métodos pensados específicamente para el manejo de colas, como append(), appendleft(), pop(), popleft(), y puede configurarse con una capacidad máxima (maxlen), convirtiéndolo en un buffer circular que descarta automáticamente los elementos antiguos.

En resumen, deque es una alternativa eficiente y flexible a las listas de Python cuando se necesitan operaciones rápidas en los extremos, manteniendo una interfaz simple y familiar.

### Ejemplo
```python
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
```
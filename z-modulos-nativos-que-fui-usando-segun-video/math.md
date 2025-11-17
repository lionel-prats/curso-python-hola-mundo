## `MODULO math` (video 16)
### Para qué sirve
El módulo math proporciona un conjunto de funciones matemáticas de nivel avanzado, implementadas con alta precisión y optimizadas en C.    
Está diseñado para realizar cálculos numéricos más complejos y exactos que los que ofrece Python de forma nativa mediante operadores básicos.  
Con math podés trabajar con:
- Funciones aritméticas avanzadas
(por ejemplo: ceil, floor, fabs, factorial, modf)
- Funciones exponenciales y logarítmicas
(exp, log, log10, pow)
- Funciones trigonométricas y angulares
(sin, cos, tan, degrees, radians)
- Funciones estadísticas básicas
(fsum, prod, isfinite, isnan, isinf)
- Constantes matemáticas estándar
(math.pi, math.e, math.tau)

Este módulo es ideal para cálculos científicos, estadísticos, financieros, simulaciones, análisis numérico y cualquier aplicación donde se requiera exactitud matemática y rendimiento.  
A diferencia de operadores integrados como ** o funciones genéricas, math ofrece comportamientos consistentes, resultados más precisos y soporte para valores especiales como NaN e infinitos.

### Ejemplo
```python
# metodos de math -> https://docs.python.org/3/library/math.html

import math

print("math.ceil(1.00001) == ", math.ceil(1.00001))
print("math.isnan(23) == ", math.isnan(23))
print("math.isnan(float('nan')) == ", math.isnan(float('nan')))
print("math.isnan(float('23')) == ", math.isnan(float('23')))
print("math.pow(10, 3) == ", math.pow(10, 3))
print("10 ** 3 == ", 10 ** 3)
print("math.sqrt(9) == ", math.sqrt(9))

"""
math.ceil(1.00001) ==  2
math.isnan(23) ==  False
math.isnan(float('nan')) ==  True
math.isnan(float('23')) ==  False
math.pow(10, 3) ==  1000.0
10 ** 3 ==  1000
math.sqrt(9) ==  3.0
"""
```
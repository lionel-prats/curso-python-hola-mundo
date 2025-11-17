# ref. v116

from datetime import datetime, timedelta
import os
os.system('cls' if os.name == 'nt' else 'clear')

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)
print(type(fecha1), type(fecha2), "\n")

delta = fecha2 - fecha1

print(type(delta), delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())

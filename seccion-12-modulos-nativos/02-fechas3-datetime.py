# ref. v115

from datetime import datetime
import os
os.system('cls' if os.name == 'nt' else 'clear')

# directivas fecha python -> https://docs.python.org/3/library/datetime.html
# tag -> The following is a list of all the format

fecha = datetime(2025, 11, 16)
fecha2 = datetime(2025, 2, 1)
ahora = datetime.now()

print(fecha)
print(fecha2)
print(ahora)

# COMO CREAR UNA FECHA A PARTIR DE UN STRING vvv

# fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
fechaStr = datetime.strptime("03-01-2023", "%d-%m-%Y")
print(type(fechaStr))
print(fechaStr)

# COMO CREAR UNA STRING A PARTIR DE UNA FECHA vvv
print(type(fechaStr.strftime("%Y-%m-%d")))
print(fechaStr.strftime("%Y-%m-%d"))

# COMPARAR FECHAS
print(fecha, fecha2, fecha < fecha2)


print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
    fecha.second
)

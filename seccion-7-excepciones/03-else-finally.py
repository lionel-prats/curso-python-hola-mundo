# ref. video 84
import os
os.system('cls' if os.name == 'nt' else 'clear')


try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("ocurrio un error inseperado")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")

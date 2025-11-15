print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")
num1 = input("Ingresa número: ")
while not num1:
    num1 = input("Ingresa número: ")
op = ""
while op.lower() != "salir":
    op = input("Ingresa operación: ")
    op = op.lower()
    while not op or op not in ["suma", "multi", "div", "resta", "salir"]:
        op = input("Ingresa operación: ")
        op = op.lower()
    if op == "salir":
        break
    num2 = input("Ingresa el siguiente número: ")
    while not num2:
        num2 = input("Ingresa el siguiente número: ")

    if op == "suma":
        num1 = int(num1) + int(num2)
    elif op == "resta":
        num1 = int(num1) - int(num2)
    elif op == "multi":
        num1 = int(num1) * int(num2)
    else:
        num1 = int(num1) / int(num2)
    print(f"El resultado es {num1}.")

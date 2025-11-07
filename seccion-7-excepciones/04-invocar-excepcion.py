# ref. video 85

# errors and exceptions, doc -> https://docs.python.org/3/library/exceptions.html

import os
os.system('cls' if os.name == 'nt' else 'clear')


def division(n=0):
    if n == 0:
        # pass
        # raise Exception("No se puede dividir por 0")
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")

    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)

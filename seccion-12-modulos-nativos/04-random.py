# ref. v117

import random
import string
import os
os.system('cls' if os.name == 'nt' else 'clear')

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)

print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    random.choices("abcdefghi.,123", k=3),
    "".join(random.choices("abcdefghi.,123", k=3)),
    "\n"
)

# hash alfanumerico de 16 caracterers vvv
chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(chars, digitos, seleccion, "".join(seleccion), "\n")

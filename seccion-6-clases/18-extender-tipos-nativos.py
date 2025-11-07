# ref. video 81

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista(list([1, 2, 3]))

lista.append(4)
lista.prepend(0)

print(lista)

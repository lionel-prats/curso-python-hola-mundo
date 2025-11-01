from pprint import pprint
import os
os.system('cls' if os.name == 'nt' else 'clear')


string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    pprint(chars_dict, width=1)
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tupla(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = f"Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key.upper()} con {valor} repeticiones \n"
    return mensaje


def get_reporte(string):
    sin_espacios = quita_espacios(string)
    contados = cuenta_caracteres(sin_espacios)
    ordenados = ordena(contados)
    mayores = mayores_tupla(ordenados)
    reporte = crea_mensaje(mayores)
    return reporte


print(get_reporte(string))

# seguir por v63 - Introducción a las clases

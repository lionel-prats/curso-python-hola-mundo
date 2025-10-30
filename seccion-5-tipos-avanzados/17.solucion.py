import os
os.system('cls' if os.name == 'nt' else 'clear')


def convertirStringEnLista(string):
    lista = [char for char in string if char != " "]
    return lista


def contarCaracteres(lista_caracteres):
    diccionario = {}
    for caracter in lista_caracteres:
        if not caracter in diccionario:
            diccionario[caracter] = 1
        else:
            diccionario[caracter] += 1
    return diccionario


def ordenarDiccionario(diccionario):
    lista = []
    for caracter, cantidad in diccionario.items():
        lista.append((caracter, cantidad))
    lista.sort(key=lambda el: (-el[1], el[0]))
    return lista


def devolverMaximos(lista):
    max_valor = max(lista, key=lambda el: el[1])[1]
    maximos = filter(lambda el: el[1] == max_valor, lista)
    return list(maximos)


def getReporte(maximos):
    maximo = maximos[0][1]
    respuesta = f"Los caracteres que más se repiten con {maximo} repeticiones son:\n"
    for caracter, maximo in maximos:
        respuesta += f"- {caracter.upper()}\n"
    return respuesta


def procesarString(string):
    lista_caracteres = convertirStringEnLista(string)
    diccionario_totales = contarCaracteres(lista_caracteres)
    lista_tuplas_ordenada = ordenarDiccionario(diccionario_totales)
    maximos = devolverMaximos(lista_tuplas_ordenada)
    reporte = getReporte(maximos)
    return reporte


string = "menem"
string = "malcorra"
string = "los muchachos peronistas"
string = "barcito"
string = "hola mundo"
string = "chanchito feliz"

print(procesarString(string))

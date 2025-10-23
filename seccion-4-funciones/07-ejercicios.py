# def es_palindromo(texto):
#     textoSinEspacios = texto.replace(" ", "").lower()
#     for char in range(len(textoSinEspacios)):
#         ultimaPosicion = len(textoSinEspacios) - 1
#         caracter1 = textoSinEspacios[char]
#         caracter2 = textoSinEspacios[ultimaPosicion - char]
#         if caracter1 != caracter2:
#             return False
#     return True

def normalizar_string(texto):
    """Convierte a minúsculas y elimina espacios."""
    return texto.replace(" ", "").lower()


def es_palindromo(texto):
    """Devuelve True si el texto es un palíndromo."""
    texto_limpio = normalizar_string(texto)
    return texto_limpio == texto_limpio[::-1]


# Pruebas
print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Menem", es_palindromo("Menem"))
print("La ruta natural", es_palindromo("La ruta natural"))
print("La ruta x natural", es_palindromo("La ruta x natural"))


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
        # = L
        # = iL
        # = oiL
        # = noiL
        # = eoniL
        # = lenoiL
    return texto_al_reves


print(reverse("Lionel"))

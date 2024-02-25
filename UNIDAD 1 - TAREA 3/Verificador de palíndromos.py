#CREA UN PROGRAMAQUE VERIFIQUE SI UNA PALABRA ES UN PALINDROMO
def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2 == 0:
        izqueierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else:
        izqueierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1]

    return izqueierda == derecha[::-1]

print(es_palindromo('oso'))
print(es_palindromo('python'))
print(es_palindromo('ojo'))
#CREA UN PROGRAMA QUE CUENTE LA CANTIDAD  DE PALABRAS  EN UNA CADENA DE TEXTO INGRESADA POR EL USUARIO 

def contador_de_palabras(texto):
    texto_limpio = texto.replace(",","")
    palabras = texto_limpio.split()
    cantidad_de_palabras = len(palabras)
    return cantidad_de_palabras

texto_ingresado = input("ingresa el texto para contar las palabras: ")
resutado = contador_de_palabras(texto_ingresado)

print(f"la cantidad de palabras en el texto es: {resutado}")
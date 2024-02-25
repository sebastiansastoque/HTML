#DESARROLLE UN PROGRAMA QUE GENERE UNA CONTRASEÑA DE SEGURIDAD 
import random, string

def creaPass(n):
    todas = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    passw = []

    for i in range(n):
        tmp = random.choice(todas)
        passw.append(tmp)
    res = "".join(passw)
    return res
n = int(input("Teclea el ancho de la contraseña: "))
test = creaPass(n)
print(test)
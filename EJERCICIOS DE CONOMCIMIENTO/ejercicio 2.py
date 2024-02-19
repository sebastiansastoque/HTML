import math
#CREAR UN PROGRAMA QUE CALCULE EL AREA DE UN CIRCULO
def calcularAreaCirculo(r):
    area=math.pi * math.pow(r, 2)
    return area

print("Ingrese radio del circulo:")
r=float(input())

print("El area del circulo es:" + str (calcularAreaCirculo(r)))

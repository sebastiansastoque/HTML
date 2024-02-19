#crear un programa modular que calcula el area de un triangulo valores de entrada del teclado.
def calcularArea(a,b):
    area=(b*a) / 2
    return area

print("Ingresar la altura:")
a=float(input())
print("ingresar la base:")
b=float(input())

print("El area es:" ,str(calcularArea(a, b)))

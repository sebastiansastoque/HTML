#Programa modular que calcule la edad dado el año,el año debe leer el usuario #A traves del teclado
def calcularEdad(nac, actual):
    edad = actual - nac
    return edad

print("ingresar el año de nacimiento:")
nac=int(input())
print("ingresar el año actual:")
actual=int(input())

print("Su edad es:" + str(calcularEdad(nac, actual)))
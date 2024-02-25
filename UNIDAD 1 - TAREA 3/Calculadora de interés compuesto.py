#CREA UN PROGRAMA QUE CALCULE EL VALOR FUTURO DE UNA INVERSION DADA
print("Ingrese el % que se desee calcular: ")
porc = float(input())
print("Ingrese el numero base: ")
num = float(input())
result = porc * num / 100
print("El",porc,"Porciento de",num,"Es",round(result, 2))
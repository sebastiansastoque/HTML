# Programa Leectura de Números Positivos
print("Debe Ingresar Dos Números Positivos")
N1 = int(input("Ingrese Número 1: "))
N2 = int(input("Ingrese Número 2: "))
while N1<0 or N2<0:
    print("Error→ Debe ingresar un número positivo, para calcular la suma.")
    N1 = int(input("Ingrese Número 1: "))
    N2 = int(input("Ingrese Número 2: "))
print(f"El valor de la suma es: { N1 + N2}")
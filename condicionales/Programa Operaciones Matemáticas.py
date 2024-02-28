#Programa Operaciones Matemáticas
#Mostramos mensaje de inicio
print("Ingrese dos números para realizar operaciones")
#Cargamos los dos números
N1 = int(input("Ingrese el primer Número: "))
N2 = int(input("Ingrese el segundo Número: "))
print("1. Suma los números Ingresados")
print("2. Restamos los números Ingresados")
print("3. Dividimos los números Ingresados")
print("4. Multiplicamos los números ingresados")
print("Otro valor, no hace nada..")
Op = int(input("Ingrese su opción.. "))
if Op==1:
    print(f"La suma de los dos números es: {N1+N2}")
elif Op==2:
    print(f"La Resta de los dos números es: {N1-N2}")
elif Op==3:
    print(f"La división de los dos números es: {N1/N2}")
elif Op==4:
    print(f"La Multiplicación de los dos números es: {N1*N2}")
else:
    print("No escogió una opción válida..")
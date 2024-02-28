# Cargaremos la edad en una variable
Edad = int(input("Ingrese una Edad:"))
# Evaluamos el contenido de la variable Edad
if Edad<18:
    print("Es Menor")
elif Edad<40:
    print("Adulto Joven..")
elif Edad<60:
    print("Adulto Experimentado")
else:
    print("Adulto Mayor")
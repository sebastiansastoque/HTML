#Programa IF anidados
#Mostramos mensaje de inicio
print("Ingrese una nota:")
Nota = float(input("Digite la definitiva:"))
if Nota>0 and Nota<3.0:
    print("Reprobó")
else:
    if Nota>=3.0 and Nota<4.0:
            print("Aprobó")
    else:
        if Nota>=4.0 and Nota<4.5:
           print("Aprobó Bien")
        else:
            if Nota>=4.5 and Nota<=5.0:
                print("Aprobó Excelente")
            else:
                print("Valor Inválido")
#ESCRIBE UN PROGRAMA QUE GENERE UN NUMERO ALEARORIO ENTRE 1 Y 100
numero = 45 #Numero que se desea adivinar
control = 0 #Variable de control de ciclo
intentos = 1 #controlar los intentos
print("Bienvenido al juego adivina numero")
while(control==0):
    print("Intento numero; ",intentos)
    print("ingrese un numero")
    num = int(input()) #Solicitamos un numero para comparar
    if(num==numero):
        print("¡Adivina el numero!")
        print("Utilizaste ",intentos," intentos")
        print("Fin del juego")
        control=1
    elif(num > numero):
        print("El numero ingresado es mayor, intenta nuvamente!")
        intentos +=1
    elif(num < numero):
        print("El numero ingresado es menor, intenta nuevamente")

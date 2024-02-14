n = int(input("ingrese la cantidad de notas que desee: "))
suma=0
i=1
while(i<=n):
    print("ingrese las notas numero" ,i)
    notas=float(input())
    suma=suma+notas
    i=i+1
    prom=suma/n
    print("el promedio de las notas",prom)

    num = prom
    prom=round(num,2)
    print(prom)

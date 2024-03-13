#CREAR UNA CODIGO QUE CALCULE EL SALARIO CON UNA HORA Y MEDIA EXTRAS
def computepay (horas_trabajadas, tarifa, salario_base):
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extras = horas_trabajadas - 40
    else:
        horas_normales = horas_trabajadas
        horas_extras = 0
    salario_base = (horas_normales * (tarifa) + (horas_extras * 1,5)) + salario_base
    return salario_base
 
 #EJEMPLO DE USO
horas_trabajadas = 45
tarifa = 10

salaio_total = horas_trabajadas
print ("el salario es: ",str(horas_trabajadas * tarifa))

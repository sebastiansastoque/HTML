#ESCRIBE UN PROGRAMA QUE GENERE LOS PRIMEROS N NUMEROS DE LA SECUENCIA FIBINACCI

a = 1 
b = 1

print(f'{a}, {b}', end=', ')

for i in range (15):
    c = a + b
    b = a
    a = c
    print(a, end=', ')


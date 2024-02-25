#PROGRAMA QUE ADMINISTRA UNA LISTA DE COMPRAS
lista_compras = []
print("--------------------")
print("-LISTA DE LA COMPRA-")
print("--------------------")
print()

while True:
    print("1. Añadir producto.")
    print("2. Eliminar producto.")
    print("3. Mostrar lista compra.")
    print("4. Salir del programa")
    print()
    opcion = input ("--> ")
    print()

    if opcion == "1":
        producto = input("Introduce el producto: ").capitalize()
        if producto in lista_compras:
            print("Ese producto ya eta en la lista")
        else:
            lista_compras.append(producto)    
    elif opcion== "2":
        producto = input("Introduce el producto: ").capitalize()
        if producto not in lista_compras:
            print("Ese producto no esta en la lista.")
        else:
            lista_compras.remove(producto)   
    elif opcion == "3":
        print("Lista compra:")
        for e in lista_compras:
            print(" -", e) 
    elif opcion == "4":
        break
    else:
        print("Introduce una opcion correcta.")
    print()    

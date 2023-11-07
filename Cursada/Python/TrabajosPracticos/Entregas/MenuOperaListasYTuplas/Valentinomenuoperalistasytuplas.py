#------------------------------------------------------------------------------------------------------------
# Fecha: 03-08-23
# Estudiante: Valentino Leiss
# Titulo: Menú para operar listas y tuplas
#------------------------------------------------------------------------------------------------------------

#Declarar y de finir una lista de ...

listas_marcas = ['BMW', 'Pagani', 'Ferrari', 'Lexus', 'Ford','Konisegg','Volkswagen','Lamborghini']

print("------------MENU--------------")
print("1-imprimir toda la lista con la funcion print")
print("2-imprimir toda la lista con el bucle FOR")
print("3-imprimir un elemento concreto de la lista")
print("4-agregar un elemento a lista en la ultima ubicación")
print("5-agregar un elemento a la lista en una ubicacion concreta")
print("6-Remplazar un elemento de la lista")
print("7-Quitar un elemento")
print("8-ordenar la lista alfabeticamente")

opcion = int(input("ingrese una opcion: "))

if opcion == 1: 
    print(listas_marcas)
elif opcion == 2:
    for marca in listas_marcas:
        print(marca)
elif opcion == 3:
    print(f"el segundo elemento de la lista: {listas_marcas[1]}")
elif opcion == 4:
    listas_marcas.append("Suzuki")
    print("se agrego correctamente el elemento")
elif opcion == 5:
    listas_marcas.insert(3, "Jeep")
    print("se agrego correctamente el elemento")
elif opcion == 6:
    listas_marcas[3] = "Rolls Royce"
    print("se reemplazo correctamente el elemento")
elif opcion == 7:
    listas_marcas.pop(5)
    print("se elimino correctamente el elemento")
elif opcion == 8:
    listas_marcas.sort()
    print("se ordeno correctamente la lista")
else:
    print("¡ La opcion ingresada es incorrecta !")
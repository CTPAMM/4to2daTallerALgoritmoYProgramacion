#------------------------------------------------------------------------------------
#Fecha:04-08-23
#Estudiante: Victoria Pibernus
#Titulo: Listas y Tuplas
#------------------------------------------------------------------------------------
#Declaro una lista de 7 elementos
Lista_provincias = ['Tierra del Fuego','San Luis','Chaco','Jujuy','Santiago del Estero','Salta']

print("--------------------------MENU----------------------------")

print("1- Imprimir toda la lista con la función print")
print("2-Imprimir toda la lista con el bucle FOR")
print("3-Imprimir un elemento concreto de la lista")
print("4- Agregar un elemento a la lista en la ultima ubicacion")
print("5-Agregar un elemento a la lista en una ubicación concreta")
print("6-Reemplazar un elemento concreto de la lista")
print("7-Quitar un elemento")
print("8-Ordenar la lista alfabeticamente")

print("--------------------------MENU----------------------------")

opcion= int(input("Ingrese una opción del menú: "))

if opción == 1:
    print(Lista_provincias)
elif opción == 2:
    for provincia in lista_provincias:
        print(provincias)
elif opción == 3:
    print(f"El segundo elemento de la lista es: {lista_marcas[1]}")
elif opción == 4:
   lista_provincias.append('Chaco')
   print('Se agregó correctamente el elemento')
elif opción == 5:
    lista_provincias.insert(3, 'Jujuy')
    print('Se agregó correctamente el elemento')
elif opción == 6:
    lista_provincias[3] = 'Salta'
    print('Se reemplazó correctamente el elemento')
elif opción == 7:
    lista_provincias.pop(3)
    print('Se eliminó correctamente el elemento')
elif opción == 8:
    lista_provincias.sort()
    print('Se ordenó correctamente la lista')
else:
    print('¡ La opción ingresada es incorrecta !')
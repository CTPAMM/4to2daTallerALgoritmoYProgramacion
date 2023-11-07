#------------------------------------------------------------------------
#Fecha:04-08-23
#Titulo:Menu para operar Listas y Tuplas
#Estudiante: Ailin Soler
#------------------------------------------------------------------------

#Declaro una lista de 11 elementos
lista_canciones_Maria_Becerra = ['episodios', 'perdidamente', 'hasta que la muerte nos separe', 'corazon vacio', 'te necesito', 'cerquita de ti', 'nada de amor','te cura', 'adios', 'dime como hago', 'mi debilidad'] 

print('***********************MENU************************')

print('1- Imprimir toda la lista con la funion print')
print('2- Imprimir toda la lista con el bucle FOR')
print('3- Imprimir un elemento concreto de la lista')
print('4- Agregar un elemento a la lista en la ultima ubicacion')
print('5- Agregar un elemento a la lista en una ubicacion concreta')
print('6- Reemplazar un elemento concreto de la lista')
print('7- Quitar un elemento')
print('8- Ordenar la lista alfabeticamente')

print('***********************MENU************************')

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
   print(lista_canciones)
elif opcion == 2:
    for marca in lista_canciones:
            print(canciones)
elif opcion == 3:
    print(f'El segundo elemento de la lista es: {lista_marcas[1]}')
    elif opcion == 4:
        lista_canciones.append('Felices x siempre')
        print('Se agrego correctamente el elemento')
elif opcion == 5:
    lista_marcas.insert(3, 'High')
    print('Se agrego correctamente el elemento')
elif opcion == 6:
    lista_canciones[3] = 'Animal'
    print('Se reemplazo correctamente el elemento')
elif opcion == 7:
    lista_canciones.pop.(3)
    print('Se elimino correctamente el elemento')
elif opcion == 8:
    lista_canciones.sort()
    print('Se ordeno correctamente')
else:
    pint('¡ La opcion ingresada es incorrecta!')
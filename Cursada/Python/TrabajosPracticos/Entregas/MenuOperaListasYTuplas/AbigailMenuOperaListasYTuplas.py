#---------------------------------------
# Titulo: Menu para operar Listas y Tuplas
# Estudiante: Abigail Rejala
# Curso: 4° 2
#----------------------------------------

# Declaro una lista de 8 elementos
lista_frutas = ['Uva','Naranja','Fresa','Kiwi','Banana','Sandia','Mora','Pomelo']

print('************Menu****************')

print('1- Imprimir toda la lista con la funcion print')
print('2- Imprimir toda la lista con el bucle FOR')
print('3- Imprimir un elemento concreto de la lista')
print('4- Agregar un elemento a la lista en la ultima ubicacion')
print('5- Agregar un elemento a la lista en una ubicacion cencreta')
print('6- Reemplazar un elemento concreto a la lista')
print('7- Quitar un elemento')
print('8- Ordenar la lista alfabeticamente')

print('**************Menu*********************')

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    print(lista_frutas)
elif opcion ==2:
    for frutas in lista_frutas:
        print(frutas)
elif opcion ==3:
    print(f'El segundo elemento de la lista es: {lista_frutas[1]}')
elif opcion ==4:
    lista_frutas.append('Uva')
    print('Se agrego correctamente el elemento')
elif opcion ==5: 
    lista_frutas.insert(3,'Manzana')
    print('Se agrego correctamente el elemento')
elif opcion ==6:
    lista_frutas[3] = 'Mango'
    print('Se reemplazo correctamente el elemento')
elif opcion ==7:
    lista_frutas.pop(3)
    print('Se elimino correctamente el elemento')
elif opcion ==8:
    lista_frutas.sort()
    print('Se ordeno correctamente el elemento')
else:
    print('¡La opcion ingresada es incorrecta!')
    
    
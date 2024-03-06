#
# titulo: menu para operar lista y tuplas
#estudiantes: su nombre
#curso: 4°2
#

# declaro una lista de 7 elementos
lista_marcas = ['arcor', 'rockerfort', 'milka', 'bombom', 'block', 'kikat', 'snicker', 'kinder']

print('************************* menu ***********************')

print('1- imprimir toda la lista con la funcion print')
print('2- imprimir toda lista con el bucle FOR')
print('3- imprimir un elemento concreto de la lista')
print('4- agregar un elemento a la lista en la utlima ubicacion')
print('5- agregar un elemento a la lista en una ubicacion concreta')
print('6 reemplazar un elemento concreto de la lista')
print('7- quitar un elemento')
print('8- ordenar la lista alfabeticamente')

print('******************************* menu *********************')

opcion = int(input("ingrese una opcion: "))

if opcion == 1:
    print(lista_marcas)
elif opcion == 2:
    for marca in lista_marcas:
        print(marca)
elif opcion == 3:
    print(f'el segundo elemento de la lista es: {lista_marcas[1]}')
elif opcion == 4:
    lista_marcas.apped('milka')
    print('se agrego correctamente el elemento')
elif opcion == 5:
    lista_marcas.insert(3, 'rocklet')
    print('se agrego corectamente el elemnto')
elif opcion == 6:
    lista_marcas[3] = 'tofi'
    print(' se remplazo correctamente el elemento')
elif opcion == 7: 
    lista_marcas.pop(3)
    print('se elimino correctamente el elemento')
elif opcion == 8:
    lista_marcas.sort()
    print('se ordeno correctamente la lista')
else:
    print(' ¡ la opcion ingresada es incorrecta !')
    
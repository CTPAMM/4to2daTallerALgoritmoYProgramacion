#------------------------------------------------------------------
# Fecha: 02-08-23
# Estudiante: Facundo Zambrano
# tutulo: listas y tuplas
#------------------------------------------------------------------

#------------------------------------------------------------------
# listas
#------------------------------------------------------------------
# declarar y definir las variables
lista_perfumes = ['Calvin Klein', 'givenchy', 'Bvlgari', 'Dolce gabbanna', 'Carolina herrera', 'Christian dior', 'Burberry']
print(lista_perfumes)

# Imprimir la lista con un bucle FOR
for marca in lista_perfumes:
    print(perfume)

    print('************************** Menu **************************')

    print('1-imprimir toda la lista con la funcion print')
    print('2-imprimir toda la lista con el bucle FOR')
    print('3-imprimir un elemento concreto de la lista')
    print('4-agregar un elemento a la lista en la ultima ubicacion')
    print('5-agregar un eemento a la lista en una ubicacion concreta')
    print('6-remplazar un elemento concreto de la lista')
    print('7-quitar un elemento')
    print('8-ordenar la lista alfabetica')
    
    print('************************** Menu **************************')

opcion=int(input('ingrese una opcion del menu:'))

if opcion == 1:
    print(lista_marcas)
elif opcion == 2:
    for marca in lista_marcas:
        print(marca)
elif opcion == 3:
    print(f'el segundo elemento de la lista es: {lista_perfumes[1]}')
elif opcion == 4:
    lista_perfumes.append('Icon')
    print('se agrego correctamente el elemento')
elif opcion == 5:
    lista_perfumes.insert(3, 'Versace')
    print('se agrego correctamente el elemento')
elif opcion == 6:
     lista_perfumes[3] = 'Polo'
     print('se reemplazo correctamente el elemento')
elif opcion == 7:
    lista_perfumes.pop(3)
    print('se elimini correctamente el elemento')
elif opcion == 8:
    lista_perfumes.sort()
    print('se orden correctamente la lista')
else:
    print('¡ La opcion ingresada es incorrecta !')
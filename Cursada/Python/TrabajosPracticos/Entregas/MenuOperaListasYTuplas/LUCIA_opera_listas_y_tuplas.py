# ------------------------------------------------
# Fecha:02-08-2023
# Estudiante: Lucia Q
# Titulo: Listas y Tuplas.
# -------------------------------------------------

# ------------------------------------------------
# LISTAS
# -------------------------------------------------

# Declarar y definir las variables.

lista_marcas = ["Adidas","Nike","Puma","Valeniaga","Guchi","Prada",]

print('***********MENU**********')
print('1- Imprimir toda la lista con la funcion print ')
print('2- Imprimir toda la lista con el bucle for ')
print('3- Imprimir un elemento concreto de la lista')
print('4- Agregar un elemento a la lista en la ultima ubicacion')
print('5- Agregar un elemento a la lista en una ubicacion concreta')
print('6- Reemplazar un elemento concreto de la lista')
print('7- Quitar un elemento')
print('8- Ordenar la lista alfabeticamente')
print('************************')

opcion = int(input(' Ingrese una opcion: '))

if opcion == 1:
    print(lista_marcas)
elif opcion == 2:
    for marcas in lista_marcas:
        print(marcas)
elif opcion == 3:
    print(f'El segundo elemento de la lista es:{lista_marcas[1]}')
elif opcion == 4:
    lista_marcas.append('Adidas')
    print('Se agrego correctamente el elemento')
elif opcion == 5:
    lista_marcas.insert(3, 'Nike')
    print('Se agrego correctamente el elemento')
elif opcion == 6:
    lista_marcas[3] = 'Puma'
    print('Se reemplazo correctamente el elemento')
elif opcion == 7:
    lista_marcas.pop[3] 
    print('Se elimino correctamente el elemento')
elif opcion == 8:
    lista_marcas.sort()
    print('Se ordeno correctamente el elemento')
else:
    print('¡La opcion ingresada es incorrecta')
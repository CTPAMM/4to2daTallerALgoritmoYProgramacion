#----------------------------------------------------------------
# Curso: 4°2°
# Estudiante: Maria Itati
# Titulo: Menu para operar Listas y Tuplas
#---------------------------------------------------------------

# Declaro una lista de 7 elementos
from os import posix_fadvise


lista_marcas = ['Gucci', 'Louis Vuitton', 'Victoria  Secret' , 'Kevingston', 'Maybelline', 'Nike', 'Mac']

print ('*********** Menu ************')

print ('1- Imprimir toda la lista con la funcion print')
print ('2- Imprimir toda la lista con el bucle FOR')
print ('3- Imprimir un elemento concreto de la lista')
print ('4- Agregar un elemento a la lista en la ultima ubicacion')
print ('5- Agregar un elemento a la lista en una ubicacion concreta')
print ('6- Reemplazar un elemento conceto de la lista')
print ('7- Quitar un elemento')
print ('8- Ordenar la lista alfabeticamente')

print('************************** Menu *****************************')

opcion = int (input("Ingrese una opcion: "))

if opcion == 1: 
    print(lista_marcas)
elif opcion == 2:
    for marca in lista_marcas:
        print(marca)
elif opcion ==3: 
    print(f'El segundo elemento de la lista es: {lista_marcas [1]}')
elif opcion == 4:
    lista_marcas.append ('Gucci')
    print('Se agrego correctamente el elemento')
elif opcion == 5:
    lista_marcas.insert(3, 'Lois Vuitton')
    print('Se agrego correctamente el elemento')
elif opcion == 6:
    lista_marcas[3] = 'Victoria Secret'
    print ('Se reemplazo correctamente el elemento')
elif opcion == 7:
    lista_marcas.pop(3)
    print ('Se elimino correctamente el elemento')
elif opcion == 8: 
    lista_marcas.sort()
    print('Se ordeno correctamente la lista')
else:
    print('¡ La opcin ingresada es incorrecta !')

#----------------------------------------------------
# Fecha 04/08/2023
# Listas Y Duplas
# Estudiante: Alexis Herculano
#----------------------------------------------------

# Definir una lista De Leyendas Argentinas

lista_leyendasArgentinas=['Messi', 'Maradona', 'Di Stefano', 'Kempes', 'Riquelme', 'Passarella', 'Batistuta', 'Fillol', 'Bochini', 'Di Maria']

print("------------Menu------------")

print('1-Imprimir lista con la funcion print')
print("2-Imprimir toda la lista con el bucle FOR")
print("3-Imprimir elemento concreto de la lista")
print("4-Agregar un elemento a la lista en la ultima ubicaion")
print("5-Agregar un elemento a la lista en una ubicacion concreta")
print("6-Remplazar un elemento concreto de la lista")
print("7-Quitar un elemento")
print("8-Ordenar la lista alcfcabeticamente")

print("----------------------------")

opcion=int(input("Ingrese Una Opcion Del Menu: "))

if opcion==1:
    print(lista_leyendasArgentinas)
elif opcion==2:
    for leyendas in lista_leyendasArgentinas:
        print(leyendas)
elif opcion==3:
    print(f'El segundo elemento de la lista es: {lista_leyendasArgentinas[1]}')
elif opcion==4:
    lista_leyendasArgentinas.append('Rattin')
    print('Se agrego correctamente un elemmento')
elif opcion==5:
    lista_leyendasArgentinas.insert(5, Palermo)
    print('Se agrego correctamente el elemento')
elif opcion==6:
    lista_leyendasArgentinas[3]= 'Zanetti'
    print('Se remplazo correctamente el elemento')
elif opcion==7:
    lista_leyendasArgentinas.pop(3)
    print('Se elimino correctamente el elemento')
elif opcion==8:
    lista_leyendasArgentinas.sort()
    print('Se ordeno correctamente la lista')
else:
    print("La opcion ingresada es incorrecta no seas salame")
#---------------------------------------------------------------------------------------------------------------------
# Fecha: 02-08-23
# Estudiante: Su nombre completo
# Titulo: Listas y tuplas.
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
# LISTAS
#--------------------------------------------------------------------------------------------------------------------
# Declarar y definir las variables
lista_marcas = [ 'Samsung', 'apple', 'xiaomi', 'motorola', 'huawei']

print('**************************** Menú *******************************')

print('1- Imprimir toda la lista con la función print')
print('2- Imprimer toda la lista con el bucle FOR')
print('3- Imprimir un elemento concreto de la lista')
print('4- Agregar un elemento a la lista en la ultima ubicacion')
print('5- Agregar un elemento a la lista en una ubicacion concreta')
print('6- Remplazar un elemento concreto de la lista')
print('7- Quitar un elemento')
print('8- Ordenar la lista alfabeticamente')

print('**************************** Menú *******************************')


opcion = int(input("ingrese una opcion: "))

if opcion == 1: 
    print(lista_marcas)
elif opcion == 2: 
    for marca in lista_marcas: 
        print(marca)
elif opcion == 3:
    print(f'el segundo elemento de la lista es: {lista_marcas[1]}')        
elif opcion == 4:
    lista_marcas.append('Honor')  
    print('Se agrego correctamente el elemento')  
 
elif opcion == 5:
    lista_marcas.insert(3, 'Oppo')   
    print('Se agrego correctamente el elemento')  
elif opcion == 6:
    lista_marcas[3] = 'Realme' 
    print('Se remplazo correctamente el elemento')  
elif opcion == 7: 
    lista_marcas.pop(3)    
    print('Se elimino correctamente el elemento')
elif opcion == 8:
    lista_marcas.sort()    
    print('Se ordeno correctamente el elemento')
else:
    print('¡ La opccion ingresada es incorrecta !')     
    


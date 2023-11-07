#Fecha: 04/08/2
#Estudiante: Noelia Escobar         |Curso: 4°2°
#Titulo: Lista de Tuplas

#Declarar y definir una lista de Razas de Gatos 

Lista_Razas = ['Persa','Esfinge','Siamés','Maine Coon','Angora','Carey','Ragdoll']

print("--------------------------Menú----------------------------")

print("1- Imprimir toda la lista con la funcion print")
print("2- Imprimir toda la lista con el bucle FOR")
print("3- Imprimir un elemento concreto de la lista")
print("4- Agrega un elemento a la lista en la última ubicación")
print("5- Agregar un elemento a la lista en una ubicación concreta")
print("6- Reemplazar un elemento concreto de la lista")
print("7- Quitar un elemento")
print("8- Ordenar la lista alfabeticamente")

print("------------------------------------------------------------")

opcion = int(input('Ingrese una opción: '))

if opcion == 1:
    print(Lista_Razas)
elif opcion == 2:
    for marca in Lista_Razas:
        print(marca)
elif opcion == 3:    
    print(f'El segundo elemento de la lista es: {Lista_Razas[1]}')
elif opcion == 4:    
    Lista_Razas.append('Siberiano')
    print('Se agrego correctamente el elemento')
elif opcion == 5:
    Lista_Razas.insert(3, 'Kohana')
    print('Se agrego correctamente el elemento')
elif opcion == 6:
    Lista_Razas[3] = 'Korat'
    print('Se agrego correctamente el elemento')
elif opcion == 7:
    Lista_Razas.pop(3)
    print('Se elimino correctamente el elemento')
elif opcion == 8:
    Lista_Razas.sort()
    print('Se ordeno correctamnte la lista')
else:
    print('¡ La opción ingresaa es incorrecta !')
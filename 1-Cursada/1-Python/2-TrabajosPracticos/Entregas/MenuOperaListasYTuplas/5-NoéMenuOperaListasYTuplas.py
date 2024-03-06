#-----------------------------------------------------------------------------------------------
# Estudiante: Noé Fabian
# Curso: 4° 2°
# Titulo: Menú para operar Listas y Tuplas
#-----------------------------------------------------------------------------------------------
# Declaro una lista de 7 elementos 
Lista_deportes=['Futbol','Karate','Voley','Rugby','Tenis','Taekwondo','Basquet']

print ('-----------------------------Menú-----------------------------')

print ('1- Imprimir toda la lista con la función print')
print ('2- Imprimir toda la lista con el bucle FOR')
print ('3- Imprimir un elemento concreto de la lista')
print ('4- Agregar un elemento a la lista en la última ubicación')
print ('5- Agregar un elemento a la lista en una ubicación concreta')
print ('6- Reemplazar un elemento concreto de la lista')
print ('7- Quitar un elemento')
print ('8- Ordenar la lista alfabeticamente')

print ('-----------------------------Menú-----------------------------')

opcion= int(input("Ingrese una opción :"))

if opcion == 1:
    print(Lista_deportes)
elif opcion== 2:
    for deporte in Lista_deportes:
        print(deporte)
elif opcion== 3:
    print(f"El segundo elemento de la lista es:{Lista_deportes[1]}")
elif opcion== 4:
    Lista_deportes.append('Hockey')   
    print('Se agregó correctamente el elemento')
elif opcion== 5:
    Lista_deportes.insert(3, 'Boxeo')
    print('Se agregó correctamente el elemento')
elif opcion== 6:
    Lista_deportes[3] = 'Esgrima'
    print('Se agregó correctamente el elemento')
elif opcion== 7:
    Lista_deportes.pop(4)
    print('Se elimino correctamente el elemento')
elif opcion== 8:
    Lista_deportes.sort()
    print('Se ordeno correctamente la lista')
else:
    print('¡ La opción ingresada es incorrecta !')
    

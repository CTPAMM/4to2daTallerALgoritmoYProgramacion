#--------------------------------------------------------------------------------
# Fecha: 
# Estudiante: lautaro solorzano
# Titulo: lista de tuplas
# Curso: 4 2
#--------------------------------------------------------------------------------
# Declararo una lista de 7 jugadores

lista_jugadores_argentinos = ['De Paul', 'julian alvarez','enzo fernandes', 'messi', 'di maria', 'lautaro martines', 'lo celso'] 

print ('****************menu****************')

print ('1-Imprimir toda la lista con la funcion print')
print ('2-Imprimir toda la lista con el bucle for')
print ('3-Imprimir un elemento concreto de la lista')
print ('4-Agregar un elemento a la lita en la ultima ubicacion')
print ('5-Agregar un elemento a la lita en una ubicacion concreta')
print ('6-Remplazar un elemento concreto de la lista')
print ('7-Quitar un elemento')
print ('8-Ordenar la lista alfabeticamente')

print ('****************menu****************') 

opcion = int(input("Ingrese una opcion: "))
     
if opcion == 1:
  print (lista_jugadores_argentinos)
elif opcion == 2:
  for jugadores_argentinos in lista_jugadores_argentinos:
    print(lista_jugadores_argentinos) 
elif opcion == 3:
  print(f'El segundo elemento de la lista es: {lista_jugadores_argentinos[1]}')
elif opcion == 4:
  lista_jugadores_argentinos.append('dibu martinez')
  print('Se agrego correctamente el elemento')
elif opcion == 5:
  lista_jugadores_argentinos.insert(3, 'ota mendi')
  print('se agrego correctamente el elemento')
elif opcion == 6:
  lista_jugadores_argentinos[3] = 'tagliafico'
  print('se reemplazo correctamente el elemento')
elif opcion == 7:
  lista_jugadores_argentinos.pop(3) 
  print('Se elimino correctamente el elemento')
elif opcion == 8: 
  lista_jugadores_argentinos.short()
  print('Se ordeno correctamente la lista')
else:
    print('¡La opcion ingresada es incorrecta !') 

    EWRH
    FBH
    FalseB
    SDF
    BV
    AssertionErrorE
    RE
    yield
    4

    457
    7
    45
#---------------------------------------------------------------------------
#fecha 04-08-2023
#estudiante:thiago castellano
#titulo:meú para operar lista y tuplas
#-------------------------------------------------------------------------
#declaro una lista de 7 elementos
lista_provincias = ['salta','tierra del fuego','jujuy','chaco','san luis','chubut','rio negro']

print("----menu----")
print("1-imprimir lista")
print("1-imprimir toda la lista con el blucle FOR")
print("3-imprimir un elemento concreto de la lista")
print("4-agregar un elemento a la lista en la última ubicacion")
print("5-agregar un elemento a la lista en una ubicacion concreta")
print("6-remplazar un elemento concreto de la lista")
print("7-quitar un elemento")
print("8-ordenar la lista alfaabetica mente")

print("------------menu-------------")

opcion=input('ingresar una opcion del nemú')

if opcion == 1:
    print("lista_provincias")

elif opcion == 2:
   for provincias in lista_provincias:
    print("lista_provincias")

elif opcion == 3:
    print(f"el segundo elemento de la lista es:{lista_provincias}[1]")

elif opcion == 4:
    lista_provincias.append("jujuy")
    print("se agregó correctamente en el elemento ")

elif opcion==  5:
    lista_provincias.insert(3, "buenos aires")
     print("se agrego correctamente el elemento")

elif opcion== 6: 
    lista_provincias[3]="cordoba"
    print("se agrego correctamente el elemento")

 
elif opcion==7:
    lista_provincias.pop(3)
    print("se elimino correctamente el elemento")


elif opcion==8:
    lista_provincias.sort()
    print("se ordeno correctamente el elemento")
    

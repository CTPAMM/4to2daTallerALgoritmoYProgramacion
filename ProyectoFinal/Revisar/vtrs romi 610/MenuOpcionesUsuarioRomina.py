# PROBLEMA: Un usuario necesita crear un menu de opciones.
# SOLUCION: Crear un algoritmo que soluciones el problema del usuario.
# ALGORITMO: Un programa en python para solucionar el problema.

while True:
    # PASO 1: Mostrar el menu de opciones al usuario:
    print("************************MENU DE MAQUILLAJE***********************")
    print("1- LABIAL")
    print("2- RIMEL")
    print("3- BASE")
    print("*****************************************************************")    
    
    # PASO 2: Pedir al usuario ingrese su opcion
    opcion = input("ingrese su opcion: ")
    
    # PASO 3: Decidir que operacion realizar
    
    if opcion == 1:
        print("se usa para pintarse los labios")
    elif opcion == 2:
        print("se usa para pintarse y que tengan mas volumen las pestañas")
    elif opcion == 3:
        print("se usa para cubrir para cubrir imperfecciones")
    else:
        print("¡Opcion incorrecta. Vuelvalo a intentar!")
        
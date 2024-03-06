# PROBLEMA: Un Usuario necesitoncrear un menú de opciónes.
# SOLUCIÓN: Crear un algoritmo que soluciónes el problema del usuario.
# ALGORITMO: Un programa de Python para solucionar el problema.

while True:
    # PASO 1: Mostrar el menú de opciónes del usuario.
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°MENÚ DE MAQUILLAJE°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("1- Rubor")
    print("2- Rimel")
    print("3- Iluminador")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

    # PASO 2: Pedir al usuario ingrese su opción.
    opcion = input("Ingrese su opción: ")
    
    # PASO 3: Decidir que operación realizar:
    
    if opcion == 1:
        print("Se usa para ponerle color a tu cara")
    elif opcion == 2:
        print("Es para que tus pestañas tengan mas volumen")
    elif opcion == 3:
        print("Para iluminar distintas partes del rostro")
    else:
        print("¡Opción incorrecta. Vuelvalo a intentar!")
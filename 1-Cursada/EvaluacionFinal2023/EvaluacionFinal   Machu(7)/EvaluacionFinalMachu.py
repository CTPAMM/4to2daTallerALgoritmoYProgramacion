# FECHA: 01-11-2023
# CURSO: 4TO 2DA
# ESTUDIANTE: Maximo Varela

# PROBLEMA: Crear un menú de opciones de evaluacion.

while True:
    # PASO 1: Mostrar menú de opciones.

    print("******MENÚ DE OPCIONES DE EVALUACION******") 
    print("1- Imprimir una lista de marcas de jugadores")
    print("2- Realizar una división de 2 números.")
    print("3- Describir que es un ALGORITMO")
    print("4- Describir que estructura utilizo para que la maquina tome decisiones.")
    print("5- Describir que estructura uso para repetir código.")
    print("6- Salir del programa")

    # PASO 2: Pedir al usuario ingrese su opción.

    opcion = int(input("Ingrese su opcion"))

    # PASO 3: Ejecutar la opcion elegida.

    if opcion == 1:
        clubes_jugadores = ['Fc Barcelona', 'Racing Club', 'River Plate', 'Real Madrid', 'Mancherster United']
        for club in clubes_jugadores:
            print(club)

    elif opcion == 2:
        num1 = int(input("Ingrese primer número"))
        num2 = int(input("Ingrese segundo número"))

        división = num1 / num2

        print(f"Mostrar el resultado de la división {num1} y {num2} es : {división}")  
    
    elif opcion == 3:
        print("Un algoritmo es algoritmo es una serie de pasos para resolver un problema")
    
    elif opcion == 4:
        print("Para que la maquina tome desiciones se usa la estructura  IF y ELIF más los PRINTS")
    
    elif opcion == 5:
        print("Para repetir el codigo se utiliza el WHILE TRUE")
    
    elif opcion == 6:
        print("Gracias por usar el programa")
        break
    
    else:
        print("opcion incorrecta, intente denuevo")
        
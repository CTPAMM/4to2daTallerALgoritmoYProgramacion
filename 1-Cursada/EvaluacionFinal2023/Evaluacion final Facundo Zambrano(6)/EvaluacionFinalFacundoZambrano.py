# FECHA: Miercoles 1 de noviembre del 2023
# CURSO: 4° 2°
# ESTUDIANTE: Facundo Zambrano

# PROBLEMA: Crear un menu de opciones de evaluacion

while True:
    # PASO 1: Mostrar el menu de opciones.
    print("Menu de opciones de marcas.")
    print("1- Imprimir una lista de marcas de skate")
    print("2- Realizar una division de 2 numeros.")
    print("3- Describir que es un algoritmo.")
    print("4- Describir que estructura utilizo para que la maquina tome desiciones.")
    print("5- Describir que estructura utilizo para repetir el codigo.")
    print("6- Salir del programa.")

    # PASO 2: Pedir al usuario ingrese su opcion.
    opcion = int(input("ingrese su opcion"))

    # paso 3: Ejecutar la opcion elegida

    if opcion ==1:
        marcas_skate = ('Santacruz', 'Element', 'Volcom', 'Vans', 'Traher', 'Carhartt',)
        
        for marca in marcas_skate:
            print(marca)
            
    elif opcion == 2:
        num1 =int(input("ingresar el primer numero: "))
        num2 =int(input("ingresar el segundo numero: "))
        
        division = num1/num2
        
        print(f"mostrar el resultado: {division}")
        
    elif opcion == 3:
            print("un algoritmo es una serie de pasos organizados, que describe el proceso que se debe seguir, para dar solucion a un problema espesifico")
    elif opcion == 4:
            print("las estructuras que utilizamos para que la maquina pueda tomar desiciones son: if, elif, else")
    elif opcion == 5:
            print("La estructura que se utiliza para repetir el codigo en bucle es: while")
    elif opcion == 6:
            print("gracias por utilizar nuetro programa")
            break
    else:
        print("opcion incorrecta, vuelva a intentar")
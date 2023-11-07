#*******************************************************
# Fecha: 01/11/23
# Estudiante: A.Lucia Quispe
# Profesor: Pablo Gay
# Curso: 4to 2da
#*******************************************************

#PROBLEMA: Crear un menú de opciones de evaluación.

while True:
    #PASO 1: Mostrar el menú de opciones.
    print("1- Imprimir una lista de marcas de ropa deportiva")
    print("2- Realizar una división de 2 números ")
    print("3- Describir que es un algoritmo ")
    print("4- Describir que estructura utilizo para que la maquina decida ")
    print("5- Describir que estructura uso para repetir codigos. ")
    print("6- Salir del programa")

#PASO 2: Pedir al usuario que ingrese su opción.

    opcion = int(input("Ingresé su opción: "))

#PASO 3: Ejecutar la opción elegida.

    if opcion == 1:
        marcas_ropa_deportiva = [ "Adidas","Nike","Puma","Asics","Jordan"]

        for marca in marcas_ropa_deportiva:
            print(marca)

    elif opcion == 2:

        numero1 = int(input("Ingresé su primer número: "))
        numero2 = int(input("Ingresé su primer número: "))

        print("El resultado de la división de los 2 numeros es: ")
        print(numero1 / numero2)

    elif opcion == 3:
        print("Un algoritmo es una serie de pasos para resolver un problema.")

    elif opcion == 4:
        print("Para que la maquina decida que opcion se utiliza la estructura es: if, elif(se coloca dependiendo cuantas opciones se necesiten)y el else")

    elif opcion == 5:
        print("Para repetir los codigos se utilza el while")
        
    elif opcion == 6:
        print("Gracias por utilizar nuestro programa.")
        break

    else:
        print("Opción incorrecta, Vuelva a intentarlo")

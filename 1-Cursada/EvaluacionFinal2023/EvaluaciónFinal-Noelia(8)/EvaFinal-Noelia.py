#Fecha: 1/11/23
#Curso: 4° 2°
#Estudiante: Noelia Escobar

#PROBLEMA: Crear un menú de opciones de evaluacion

while True:
    
#PASO1: Mostrar un menú de opciones.

    print("                                                 ")
    print("             Menú de Evalucacion                 ")
    print("1-Imprimir una lista de marcas de autos")
    print("2-Realizar una division de 2 numeros")
    print("3-Describir que es una algoritmo.")
    print("4.Describir que estructura utilizo para que la maquina tome deciciones.")
    print("5-Que estructura uso para repetir codigo.")
    print("6-Salir de programa.")
    print("                    ")

    #PASO2:Pedir al usuario ingrese su opcion

    opcion =int(input("Ingrese su opcion: "))

    #PASO 3: Ejecutar la opcion elegida.

    if opcion == 1:
        marcas_autos = ['Nissan','Toyota','BMW','Fiat','Renault','Honda']

        for marca in marcas_autos:
            print(marca)
    
    elif opcion == 2:
        print("                                    ")
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))

        Division = numero1/numero2
        print("                                                                        ")
        print(f"El resultado de division es {numero1} dividido {numero2} es: {Division}")
         
    elif opcion == 3:
        print("                                          ")
        print("             Un algoritmo                ")
        print("Un algoritmo es una secuencia depasos para resolver un problema")

    elif opcion == 4:
        print("                                                                                     ")
        print("Utilizamos la estructura 'IF', 'ELIF' para tomar decisiones y 'ELSE' para otra opción")

    elif opcion == 5:
        print("                                                              ")
        print("Utilizamos la estructura 'WHILE TRUE:' para repetir un codigo.")

    elif opcion == 6:
        print("Gracias por utilizar nuestro programa")
        break

    else:
        print("                                      ")
        print("Opcion incorrecta, vuelva a intentarlo")
        

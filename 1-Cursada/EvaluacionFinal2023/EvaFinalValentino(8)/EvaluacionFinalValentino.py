# FECHA: 1/11/2023
# CURSO: 4° 2°
# ESTUDIANTE: Valentino Leiss

# PROBLEMA:  Crear un menú de opciones de evaluacion

while True:
    #PASO 1: mostrar el menú de opciones
    print("***************MENU DE OPCIONES DE EVALUACION***************")
    print("1- IMPRIMIR UNA LISTA DE MARCAS DE AUTOS")
    print("2- REALIZAR UNA DIVISION DE DOS NUMEROS")
    print("3- DESCRIBIR QUE ES UN ALGORITMO")
    print("4- DESCRIBIR QUE ESTRUCTURA UTILIZO PARA QUE LA MAQUINA TOME DESICIONES")
    print("5- DESCRIBIR QUE USO PARA REPETIR UN CODIGO")
    print("6- SALIR DEL PROGRAMA")
    
    #PASO 2: Pedir al usuario que ingrese una opcion 
    
    opcion = int(input("ingrese su opcion: "))
    
    #PASO 3: Ejecutar la opcion elegida
    
    if opcion == 1:
        marca_autos = ['BWM','FERRAR','PAGANI','MERCEDES-BENZ','KOENIGSEGG']
        for marca in marca_autos:
            print(marca)
    elif opcion == 2:
        numero1 = int(input("introduzca su primer numero: "))
        numero2 = int(input("introduzca su segundo numero: "))
        resultado = numero1 / numero2
        print(f"la division de {numero1} y {numero2} es: {resultado}")
    elif opcion == 3:
        print("Los algoritmos son un conjunto de instrucciones sistematicas y previamente definidas que se utilizan para realizar una determinada tarea")
    elif opcion == 4:
        print("Para que la maquina tome desiciones se utiliza: opcion, int, input, if, elif y else")
    elif opcion == 5:
        print("Para repetir codigos se utiliza: while True")
    elif opcion == 6:
        break
    else:
        print("Opcion incorrecta.")
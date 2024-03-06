#calculadora para relizar operaciones matematicas

# Iterar infinitamente todo el programa

while True:
    # Imprimir en pantalla el menú de opciones

    print("**********************************************************")
    print("bienvenido a la calculadora de 6 operaciones")
    print("                                                          ")
    print("**********************************************************")

    print("******************menu de operaciones********************")
    print("1- suma")
    print("2- resta")
    print("3-multiplicacion")
    print("4-division")
    print("5-potenciacion")
    print("6-raciacion")
    print("**********************************************")

    # Pedir al usuario ingrese una opción del menú

    opcion = int(input("*ingrese una opcion de operacion: ") )
                
    print("***********inicia la aplicacion*********************")

    # Pedir al usuario ingrese los números a operar

    numero1 = input("ingrese el primer numero")
    numero2 = input("ingrese el segundo numero")

    # Decidir la operación a realizar según la opción ingresada por el usuario

    if opcion == 1:
        suma =numero1+numero2
        print(f"el resultado de sumar {numero1} y {numero2} es: {suma}")
    elif opcion == 2:
        resta = numero1-numero2
        print(f"el resultado de restar {numero1} y {numero2} es {resta} ")
    elif opcion == 3:
        multiplicacion = numero1*numero2
        print(f"el resultado de multiplicar {numero1} y {numero2} es {multiplicacion} ")
    elif opcion == 4:
        potenciacion  # Profe: falta operación de división
        print(f"el resultado de dividir {numero1} y {numero2} es {divicion} ")
    elif opcion == 5:
        divicion == numero1^numero2  # Profe: falta operador de potenciación (**)
        print(f"el resultado de la potenciacion {numero1} y {numero2}  es {potenciacion}")
    elif opcion == 6:
        radicacion = numero1 numero2  # Profe: falta operación de radicación
        print(f"el resultado de radicacion {numero1} y {numero2}  es {radicacion}")
    else # Profe: Falta la lógica para el "else"
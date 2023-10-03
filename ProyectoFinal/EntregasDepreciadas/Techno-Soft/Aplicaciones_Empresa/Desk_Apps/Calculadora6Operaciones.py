# Calculadora para realizar operaciones matemáticas (6)

# Iterar infinitamente todo el programa

while True:
    # Imprimir en pantalla el menú de opciones

    print("****************************************************************")
    print("Bienvenido a la calculadora de 6 operaciones")
    print("****************************************************************")

    print("********************** MENU DE OPERACIONES **********************")
    print("1- SUMA")
    print("2- RESTA")
    print("3- MULTIPLICACIÓN")
    print("4- DIVISIÓN")
    print("5- POTENCIACIÓN")
    print("6- RADICACIÓN")
    print("****************************************************************")

    # Pedir al usuario ingrese una opción del menú

    opcion = int(input("Ingrese una opción de operación: "))

    print("********************** Inicia aplicación **********************")

    # Pedir al usuario ingrese los números a operar

    numero1 = input(" Ingrese el primer número: ")  # Profe: cambiar a int los inputs
    numero2 = input(" Ingrese el segundo número: ")

    # Decidir la operación a realizar según la opción ingresada por el usuario

    if opcion == 1:
        Suma = numero1+numero2
        print(f"El resultado d la suma {numero1} y {numero2} es: {Suma}")
    elif opcion == 2:
        resta = numero1-numero2
        print(f"El resultado de la resta {numero1} y {numero2} es: {resta}")
    elif opcion == 3:
        Multiplicacoin = numero1*numero2
        print(f"El resultado de la multiplicacion {numero1} y {numero2} es: {Multiplicacoin}")
    elif opcion == 4:
        Division = numero1/numero2
        print(f"El resultado de division {numero1} y {numero2} es: {Division}")    
    elif opcion == 5:
        Potenciación = numero1^numero2  # Profe: Falta operador de potenciación (**)
        print(f"El resultado de potencia {numero1} y {numero2} es: {Potenciación}")
    elif opcion == 6:
        Radicación = numero1numero2  # Profe: Falta la operación de radicación
        print(f"El resultado de radicación {numero1} y {numero2} es: {Radicación}")
    else # Profe: Falta la lógica para el "else"
        
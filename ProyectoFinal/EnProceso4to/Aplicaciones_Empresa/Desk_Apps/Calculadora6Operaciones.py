# Calculadora para realizar operaciones matemáticas (6)
while True:
    print("**********************************************")
    print("Bienvenido a la calculadora de 6 operaciones")
    print("                             Hecha por OvniOn")
    print("**********************************************")

    print("************ MENÚ DE OPERACIONES **************")
    print("1- SUMA")
    print("2- RESTA")
    print("3- MULTIPLICACIÓN")
    print("4- DIVISIÓN")
    print("5- POTENCIACIÓN")
    print("6- RADICACIÓN")
    print("**********************************************")

    opcion = int(input("Ingrese una opción de operación: "))

    # Comienza la lógica del programa.

    print("************* Inicia aplicación *************")

    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    if opcion == 1:
        suma = numero1 + numero2
        print(f"El resultado de sumar {numero1} y {numero2} es: {suma}")
    elif opcion == 2:
        resta = numero1 - numero2
        print(f"El resultado de restar {numero1} y {numero2} es: {resta}")
    elif opcion == 3:
        multiplicacion = numero1 * numero2
        print(f"El resultado de multiplicar {numero1} y {numero2} es: {multiplicacion}")
    elif opcion == 4:     
        
    elif opcion == 5:  
        
    elif opcion == 6:  
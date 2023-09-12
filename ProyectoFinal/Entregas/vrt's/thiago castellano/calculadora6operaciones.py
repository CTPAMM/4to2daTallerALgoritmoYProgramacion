# calculadora para realizar operaciones matematicas (6)
while True: 

    print("************************************************")
    print("bienvenido a la calculadora de 6 operaciones")
    print("*************************************************")

    print("*********** MENÚ DE OPERACIONES***************")
    print("1 - SUMA")
    print("2- RESTA")
    print("3- MULTIPLICACION")
    print("4- DIVISION")
    print("5- POTENCIACION")
    print("6- RADICACION")
    print("************************************************")

    opcion = int(input("ingrese una opcion de operacion :"))

    # comienza la lógica del programa.

    print("**********inicia la aplicación******************")

    numero1 = input("ingresa el primer número: ")
    numero2 = input("ingresa el segundo númeero: ")
    
    if opcion == 1:
        suma = numero1 + numero2
        print(f"el resultado de suma {numero1} y {numero2}es: {suma}")
    elif opcion == 2:
        restar = numero1 - numero2
        print(f"el resultado de restar {numero1} y {numero2}")
    elif opcion == 3:
        multiplicacion = numero1 * numero2
        print(f" el resultado de multiplicar {numero1} y {numero2}")
    elif opcion == 4:
        divición = numero1 / numero2
        print(f"el relsultado de divicón {numero1} y {numero2}")
    elif opcion == 5:
        poteciacion = numero1  numero2 
        print(f"el relsutado de poteciacion {numero1} y {numero2}")
    elif opcion == 6:
        radicacio = numero1  numero2 
        print(f" el relsutado de raadicacion {numero1} y {numero2}")
        



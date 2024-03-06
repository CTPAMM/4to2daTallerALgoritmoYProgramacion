# PROBLEMA:Un usuario necesita calcular la suma y la resta de 2 números.
# SOLUCIÓN: Crear un algoritmo que solucione la suma y la resta.


    # PASO 1: Pedir al usuario que ingrese los números a operar.
    
while True:

    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))

    # PASO 2: Mostrar el menú de opciones.

    print("Menú de opciones")
    print("Ingrese 2 para sumar")
    print("Ingrese 4 para restar")

    # PASO 3: Pedir al usuario ingresar la opción elegida.

    opcion = int(input("Ingrese la opción: "))

    # PASO 4: Realizar la operación seleccionada por el usuario.

    if opcion == 2:
        resultado = numero_1 + numero_2
        print("La suma de los números es igual a: ")
        print(numero_1 + numero_2)
    else:
        resultado = numero_1 - numero_2
        print("La resta de los números es igual a: ")
        print(numero_1 - numero_2)
        
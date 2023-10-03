# PROBLEMA :Un usuario necesaria calcular la MULTIPLICACION  y la DIVICION de:
# SOLUCION : crear un algoritmo que solucione la multiplicacion y la divicion. 

while True:

    # PASO 1 : pedir al usuario que ingrese los números a operar.

    numero1 = int(input("ingrese su numero1"))
    numero2 = int(input("ingrese su numero2"))

    # PASO 2 : Mostar el menú de opciones.

    print("si desea multiplicar ingrese 1")

    print("si desea dividir ingrese 2")

    # PASO 3: pedir al usuario ingresa la opcion elegida.

    opcion = int(input("ingrese su opcion"))

    # PASO 4: realizar la operacion selecionada por el usuario.

    if opcion==1: 
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2
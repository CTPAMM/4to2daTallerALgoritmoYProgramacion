#PROBLEMA:Un usuario necesita calcular la SUMA y la RESTA de 2 numeros
#SOLUCION:Crear un algoritmo que solucione la suma y la resta

while True:
    # PASO 1 :Pedir al usuario que ingrese los numeros a operar

    numero1 = int(input("ingresa numero1"))

    numero2 = int(input("ingrese numero2"))


    # PASO 2:Mostrar el menu de opciones

    print("si desea sumar ingrese 1")

    print("si desea restar ingrese 2")

    # PASO 3:Pedir al usuario ingresar la opcion elegida.abs

    opcion = int(input("ingrese su opcion"))

    # PASO 4:Realizar la operacion seleccionada por el usuario

    if opcion==1: 
        resultado = numero1 + numero2
    else:
        resultado = numero1 - numero2

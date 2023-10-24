# PROBLEMA: un usuario necesita hacer un juego del tipo "elige tu propio destino"
# SOLUCION: crear un algoritmo para el juego
# ALGORITMO: hacer un programa En phyton

while True:
    # paso 1: pedir al usuario que ingrese su nombre 

    nombre = input ("")

    # PASO 2: saludar al usuario 

    print(f"bienvenido {nombre}")

    # PASO 3: iniciar la historia

    respuesta = input("estas comprando zapatillas, tienes que elegir entre las zapatillas blancas o negras. ¿cual eliges?")

    if respuesta ==  blancas:
        print("se las pone al salir, pisa barro y se le ensucian")
        break
    elif respuesta == negras:
        respuesta = input ("se las pone y sale de la tienda con las zapatillas puestas")
        if respuesta == "si":
            print("perdiste el juego, se te mancharon las zapatillas nuevas")
            break
        elif respuesta == "no":
        print("ganaste el juego, no se mancharon tus nuevas zapatillas")
        break
      
# PROBLEMA: Un usuario necesita hacer un juego del tipo "Elige tu propio camino"
# SOLUCIÓN: Crear un algoritmo para el juego.
# ALGORRITMO: Hacer un programa en Pyhton.

while True:
    # PASO 1: Pedir al usuario que imprese su nombre.

    nombre = input("¿Cual es su nombre? ")

    # PASO 2: Saludar al usuario.

    print(f"¡Bienvenido {nombre}!")

    # PASO 3: Iniciar la historia.

    respuesta = input("Eatás con tus amigos y no saben que hacer pero te gustaria sugerirles ir a tomar helado. ¿Les preguntarias para ir a tomar helado? (si/no)")

    if respuesta == "si":
        print("Les gusto tu idea de ir a tomar helado .Ahora te preguntan si ir a Grido o Gallet ¿Qué elegis? (Grido/ Gallet)")


    elif respuesta == "no":
        respuesta == input("Tus amigos decidieron ir a caminar por el centro. ¿Queres ir? (SI /NO)")

        if respuesta== "si":
            print("")
        
        elif respuesta == "no":
            print("")

    if respuesta == "si":
        print("")

    elif respuesta == "no":
        respuesta == input("")

        if respuesta== "si":
            print("")
        
        elif respuesta == "no":
            print("")

        if respuesta == "si":
        print("")


    elif respuesta == "no":
        respuesta == input("")

        if respuesta== "si":
            print("")
        
        elif respuesta == "no":
            print("")
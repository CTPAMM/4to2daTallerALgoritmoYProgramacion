# PROBLEMA: Un usuario necesita hacer un juego del tipo "Elige"
# SOLUCION: Crear un algoritmo para el juego
# ALGORITMO: Hacer un programa en Python

while True:
    # PASO 1: Pedir al usuario que ingrese su nombre

    nombre = input("Nombre")

    # PASO 2: Saludar al usaurio

    print(f"Biemvenido {nombre}")

    # PASO 3: Inciar la historia.

    respuesta = input("tenes que ir a la libreria a comprar una cartulina pero enseguida cierra y estas en tu casa que esta en buenos aires a 35 cuadras de la libreria mas cercana y no tenes auto, ¿te vas en colectivo o caminando?")

    if respuesta == "ir caminando":
        print("fuiste caminando hasta una linea de subte y te subiste al subte, te bajaste cerca de la libreria, ¿vas por un pasillos estrecho y oscuro para llegar llendo recto, o le das la vuelta a la manzana para llegar?")
        break
    elif respuesta == "subirse al colectivo":
        respuesta = input("te subiste al colectivo y un fisura te durmio las llantas y la villetera, no te llego la guita para comprar la cartulina, perdiste el juego")
        if respuesta == "Dar la vuelta a la manzana":
            print("intentando dar la vuelta a la manzana llegaste a la esquina y un chavon te quiso vender unos pares de medias y como andabas cortina de guita le dijiste que no y te robo la billetera, no te quedo un mango para comprar la cartulina, perdiste el juego")
            break
        elif respuesta == "Pasar por el pasillo":
            print("pasaste por el pasillo y te encontraste a un caniche lo acariciaste, seguiste derecho y llegaste a comprar la cartulina, ganaste el juego.")
            break
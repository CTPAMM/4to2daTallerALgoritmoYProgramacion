# PROBLEMA: Un usuaario necesita hacer un juego del tipo "Elige tu propia aventura"
# SOLUCIÓN: Crear un algoritmo para el juego
# ALGORITMO: Hacer un programa de Python

while True:
    # PASO 1: Pedir al usuario que ingrese su nombre

    nombre = input("Ingrese se nombre")

    # PASO 2: Saludar al usuario

    print(f"Bienvenido usuario")

    # PASO 3: Iniciar la historia.

    respuesta = input("Hay un lobo y tres chanchitos, ellos deberan escapar de él eligiendo una de las dos opciónes, una casa de paja o una casa de madera"("casa de madera/casa de paja")

    if respuesta == "casa de paja":
        print("el lobo destruyó la casa y deboró a los chanchitos")
        break 
    elif respuesta == "casa de madera":
        respuesta = input("tenes mas posibilidades de que el lobo no los ataque, deberas elegir si esconderte en el baño o escapar por la puerta trasera antes de que el lobo intente entrar, ¿esconderte en el baño/escapar por la puerta trasera")
        if respuesta == "esconderte en el baño":
            print("el lobo va a encontrarte en cualquier momento")
            break
        elif respuesta == "escapar por la puerta trasera":
        print("elegiste la opcion correcta, los chanchitos estan libres")
        break


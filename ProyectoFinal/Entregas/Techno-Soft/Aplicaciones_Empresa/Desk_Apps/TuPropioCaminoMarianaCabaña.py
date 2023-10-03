# PROBLEMA: Un usuario necesita hacer un juego del tipo "Elige tu propia historia".
# SOLUCIÓN: Crear un algoritmo para el juego
# ALGORITMO: Hacer un programa en Python

while True:
    # PASO 1: Pedir al usuario que ingrese su nombre.
    
    nombre = input("Ingresa tu nombre: ")
    
    # PASO 2: Saludar al usuario
    
    print(f"Bienvenida {nombre}")
    
    # PASO 3: Iniciar la historia.
    
    respuesta = print("Estás en un lugar oscuro, no sabes a donde ir y solo tienes 2 puertas al frente tuyo. ¿A cuál entrarías? (izquierda/derecha)")
    
    if respuesta == "izquierda":
        print("Perdiste Fuiste directamente a un mundo de fantasía, donde obtienes todo lo que quieres")
        break
    elif respuesta == "derecha":
        respuesta = input("Fuiste directamente a una ciudad con un clima nublado, mostrando la realidad (si/no)")
        if respuesta == "si":
            print("Perdiste, ya que hay probabilidad de que ya no salgas de ahí ni aunque quisieras o ya estés harto")
            break
        elif respuesta == "no":
            print("Ganaste, ya que la realidad podrá verse dificil, pero es la mejor decisión que tomaste al querer probar cosas nuevas")
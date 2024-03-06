# PROBLEMA: Un Usuario necesita hacer un juego del tipo "elige
# SOLUCION: crear un algoritmo para el juego 
# ALGORITMO: Hacer un programa para el juego

while True:
    # PASO 1: pedir al usuario que ingrese su nombre 
     
     nombre = input("ingrese su nombre")
    
    # PASO 2: saludar al usuario 
    
     print(f"vienvenido al juego del reino ")

    # PASO 3: Iniciar la historia 
     
    respuesta = input("estas caminado en el reino le roban un cojar a la princesa y vos lo ves todo que haces elije una opcion ¿la ayudad a recupera el cojar? o ¿te vas?(ayudas/te vas)")
                  
    if respuesta == "te vas":
        print("los guardias vieron como te fuiste y te mandaro al calabozo")
        break
    elif respuesta == "ayudas":
        respuesta = input("el rei ve como ayudaste a la princesa y te va una recompesa")
        break
    elif respuesta == "tomaste la recompesa":
         respuesta = input("el rei te regala 2 bolsa de oro y un cabajo para mas aventuras")
         break
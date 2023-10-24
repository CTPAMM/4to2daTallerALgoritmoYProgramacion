#Problema: Un usuario necesita hacer un juego del tipo "Elige tu propia historia" 
#Solucion: Crear un algoritmo para el juego 
#Algoritmo: Hcaer un programa en Python

while True:
    #Paso 1: Pedir al usuario que ingrese su nombre 
    
   nombre = input("Ingrese un nombre: ")
   
   #Paso 2: Saludar al usuario 
   
   print(f"Bienvenido/a {nombre}")
   
   #Paso 3: Iniciar la historia 
   
   respuesta = input("Saliste de casa, ahora estas volviendo, pero esta esperando el autobús a las 1:00 AM porque no tienes auto. El autobús llego a los 6 minutos, antes de subirte al autobús, el conductor te miro con una cara que de sorprendido ¿Vas a subir al autobús? (Si/No)")
   
   if respuesta == "Si":
       print("El conductor era tu padre, se sorprendio de verte a estas horas en la calle")
       break
   elif respuesta == "No":
       respuesta = input("Era el ultimo bús..., el conductor ya se iba a su casa, pero acepto llevarte ¿Aceptas que te lleve? (Si/No)")
       if respuesta == "Si":
           print("Desapareciste")
           break
       elif respuesta == "No":
           respuesta ==input("Justo un amigo te vio en la parada, te llevo hasta tu casa")
           break
# FECHA: 01-11-2023
# CURSO: 4to 2da
# ESTUDIANTE: Gimenez Mia

# PROBLEMA: Crear un menu de opciones de evaluacion.

while True:
    # PASO 1: Mostrar el menu de opciones
    
    print("****************Menu de opciones de evaluacion****************") 
    print("1-imprimir una lista de marcas de ropa")
    print("2-Ralizar una division de dos numeros")
    print("3-describir que es un algoritmo")
    print("4- describir que estructura utilizo para que la maquina tome decisiones")
    print("5-describir que estructura utilizo para repetir el codigo")
    print("6-salir del programa")
    
    
    
    
    
    # PASO 2: Pedir al usuario que ingrese su opcion.
    
    opcion = int(input("ingrese su opcion"))
    
    # PASO 3: ejecutar la opcion elegida.
    
    
    if  opcion == 1: 
         marcas_ropas  =['nike','adidas','poper','puma','la coste']
         for marca in marcas_ropas:
             print(marca)
         
    
    elif opcion == 2:
        numero1 = int(input(" Ingrese el primer numero"))
        numero2 = int(input(" Ingrese el segundo numero"))
        division = numero1/numero2
        print(f"resultado de la division {numero1} y {numero2} es : {division}")
        
        
    elif opcion == 3: 
        print("un algoritmo es una serie de pasos para resolver un problema")
        
    elif opcion == 4: 
        print(" para que la maquina tome decisionese usa la estructura IF y ELIF mas los PRINT")
        
    elif opcion == 5:
        print(" la estructura que se utiliza para repetir el codigo es WHILE TRUE")
        
        
    elif opcion == 6:
        print("gracias por utilizar nuestro programa")
        break
    
    else:
        print("opcion incorrecta,vuelvan a intentarlo")
 
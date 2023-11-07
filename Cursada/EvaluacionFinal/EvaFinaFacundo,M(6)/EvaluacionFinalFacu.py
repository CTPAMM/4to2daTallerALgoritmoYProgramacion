# FECHA:1/11/23
# CURSO: 4TO 2DA
# ESTUDIANTE: FACUNDO MARILEO

# PROBLEMA: crear un menu de opciones de evaluacion 

while True:
    #PASO 1: mostrar el menu de opciones.
    print("***************MENU DE OPCIONES DE EVALUACION******************0")
    print("1-IMPRIMIR UNA LISTA DE MARCAS")
    print("2-realizar una division de 2 numeros")
    print("3-describir que es un algoritmo ")
    print("4-describir que estuctura utilizo para que la maquina decida o tome desiciones")
    print("5-describir que estructura uso para repetir el codigo")
    print("6-salir del programa")
    
    #PASO 2: pedir al usuario que ingrese su opcion
    opcion = int(input("ingresar opcion"))
    
    #PASO 3: EJECUTAR LA OPCION ELEGIDA
    
    if opcion == 1:
        marcas_autos = ["chevrolet","audi","subaru","BMW","ferrari"]
  
        for marca in marcas_autos:
            print(marca)      
    elif opcion == 2:
        num1 = int(input("introducir un numero"))
        num2 = int(input("introducir otro numero"))
        resultado = num1 / num2
        # Profe: Faltó imprimir el resultado.
        
    elif opcion == 3:
         print("un algoritmo es una serie de pasos para resolver un problema") 
    elif opcion == 4:
         print("para que tome decisiones se utiliza: opcion, int, input, if, elif, else" )
    elif opcion == 5:
         print("se utiliza el while true")   
    elif opcion == 6:
         print("gracias por ejecutar el programa") 
         break
    else: 
        print("opcion incorrecta")
#fecha:1/11/23
#curzo:4-2
#estudiante:walter amteo jordan

#PROBLEMA: Crear un menu de opciones de evaluacion

while True:
    #PASO 1: Mostrar menu de opciones
    
    print("*********************MENU de opciones de evaluacion*********************************")
    print("1_imprimir una lista de marca de boxeo")
    print("2_realizar una division de 2 numeros")
    print("3_describir que es un algoritmo")
    print("4_describir que estructura utilizo para que la maquina tome deciciones")
    print("5_describir que estructura uso ´para repetir codigo")
    print("6_salir del programa")
    print("************************************************************************************")
    
    #PASO 2 : pedir al usuario ingrese su opcion
    
    opcion = int(input("ingrese su opcion"))
    
    
    #paso #:EJECUTAR la opcion elegida
    if opcion == 1:
        marcas_guantes_de_boxeo = ['everlast','RDX','venum','Buddha sport','leone',]
        
        for marca in marcas_guantes_de_boxeo:
            print(marca)
        
    elif opcion == 2:
        numero1 = int(input("introduzca su primer numero"))
        numero2 = int(input("introduzca su segundo numero"))
        Resultado = numero1 / numero2
        print(f"la division entre {numero1} y {numero2} es : {Resultado}")
        
    elif opcion == 3:
        print("los algoritmo son un conjunto de intrucciones sistematicas y previamente definidas que utilizan para realizar una determinada tarea")
        
    elif opcion == 4:
        print("para que la maquina tine desiciones se utiliza: opcion,int, input,if,elif,y else")
    elif opcion == 5:
        print("para repetir codigos de programacion se utlizia: while")
    elif opcion == 6:
        break
        
    else:
        print("opcion incorrecta")
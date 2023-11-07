# FECHA: 01/11
# CURSO: 4to 2da
# ESTUDIANTE: Ailin Soler

# PROBLEMA: Crear un menu de opciones de evaluacion

while True:
    # PASO 1: Mostrar el menu de opciones.
    print("***********MENU DE OPCIONES*************")
    print("1- Imprimir una lista de marcas de zapatillas")
    print("2- Realizar una division de 2 numeros.")
    print("3- Describir que es un algoritmo")
    print("4- Describir que estructura utilizo para que la maquina decida o tome decisiones")
    print("5- Describir que estructura uso para repetir codigo.")
    print("6- Salir del programa")
    
    # PASO 2: Pedir al usuario ingrese su opcion
    opcion = int(input("Ingrese su opcion: "))
    
    # PASO 3: Ejecutar la opcion elegida
     
    if opcion == 1:
        marcas_zapatillas = ['Nike, Adidas, DC, Fila, Vans, Converse']
        
        for marca in marcas_zapatillas:
            print(marca)
    
    elif opcion == 2:
        num1 =int(input("Ingresar el 1 numero"))
        num2 =int(input("Ingresar el 2 numero"))
    
        division = num1 / num2
        
        print(f"El resultado de dividir {num1} y {num2} es:{division}")
    
    elif opcion == 3:
        print("Un algoritmo es un conjunto de pasos para resolver un problema o realizar una tarea especifica")
        
    elif opcion == 4:
        print("Para que la maquina tome decisiones las opciones son: elif, else, if")
        
    elif opcion == 5:
       print("La etiqueta que se utiliza para repetir el codigo es:while,True")
        
    elif opcion == 6:
        print("Gracias por utilizar nuestro programa")
        break
    
    else:
        print("opcion incorrecta,vuelva a intentarlo")

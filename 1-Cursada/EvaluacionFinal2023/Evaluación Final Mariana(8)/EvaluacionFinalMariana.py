# FECHA: 01-11-2023
# CURSO: 4°2°
# ESTUDIANTE: Mariana Cabaña 

# PROBLEMA: Crear un menú de evaluación

while True:
    # PASO 1: Mostrar el menú de opciones.
    
    print("**********MENÚ DE OPCIONES DE EVALUACIÓN***********")
    print("1-Imprimir una lista de marcas de ropa")
    print("2-Realizar una división de dos números")
    print("3- Describir qué es un algoritmo")
    print("4- Describir qué estructura utilizo para que la maquina tome decisiones")
    print("5- Describir qué estructura uso para repetir código")
    print("6- Salir del programa")
    print("***************************************************")
    
    # PASO 2: Pedir al usuario ingrese su opción.
    
    opcion = int(input("Ingrese su opción: "))
    
    # PASO 3: Ejecutar la opción elegida.
    
    if opcion == 1:
        marcas_ropa = ['Gucci', 'Prada', 'Fendi', 'Louis Vuitton']
        
        for marca in marcas_ropa:
            print(marca)
        
    elif opcion == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La respuesta de la división es: ")
        division = print(num1 / num2)
        
    elif opcion == 3:
        print("Algoritmo: es una instruccion para realizar algún programa")
        
    elif opcion == 4:
        print("La estructura que se usa para que la maquina tome deciciones es el 'if' y 'else'")
        
    elif opcion == 5:
        print("La estructura que se usa para repetir código, es el 'whileTrue'")
        
    elif opcion == 6:
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Opcion incorrecta. Vuelvalo a intentar")
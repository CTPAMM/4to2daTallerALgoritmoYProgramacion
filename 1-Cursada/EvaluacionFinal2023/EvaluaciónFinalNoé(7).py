# Fecha: 01/11
# Curso: 4to 2da
# Estudiante: Noé Fabian

# PROBLEMA: Crear un menú de opciones de evaluación

while True:
    # Paso 1: Mostrar el menú de opciones.
    print("***************MENÚ DE OPCIONES DE EVALUACIÓN***************")
    print("1- Imprimir una lista de marcas de autos.")
    print("2- Realizar una división de 2 números.")
    print("3- Describir que es un algoritmo.")
    print("4- Describir que estructura utilizo para que la máquina tome decisiones.")
    print("5- Describir que estructura usó para repetir el código.")
    print("6- Salir del programa.")

    # Paso 2: Pedir al usuario ingrese su opción:
    opcion = int(input("Ingrese una opción : "))
    
    # Paso 3: Ejecutar la opción elegida.
    
    if opcion == 1:
        marcas_autos = ['Ferrari', 'BMW','Lamborghini','Nissan','Ford'] 
        
        for marca in marcas_autos:
            print(marca)
            
    elif opcion == 2:
        num1 =int(input("Ingresar el primero número : "))
        num2 =int(input("Ingresar el segundo número : "))
        
        division = num1 / num2
        
        print(f"El resultado de dividir {num1} y {num2} es: {division}")

        
    elif opcion == 3:
        print("Un algoritmo es una serie de pasos para resolver un problema.")
        
    elif opcion == 4:
        print("Para que la maquina tome decisiones usamos if,elif y else.")
        
    elif opcion == 5:
        print("La etiqueta que se usa para repetir un codigo es while true.")
      
    elif opcion == 6:
        print("gracias por utilizar este programa.")
        break    
                    
    else:
        print("Opción incorrecta,vuelva a intentarlo.")       
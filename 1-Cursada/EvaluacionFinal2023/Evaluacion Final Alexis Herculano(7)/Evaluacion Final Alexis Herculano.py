# FECHA: 01/11/2023
# CURSO: 4'2
# ESTUDIANTE: Alexis Valentin Herculano

# PROBLEMA: Crear un menu de opciones de evaluacion

while True:
    
    # PASO 1: Mostrar el menu de opcines.

    print("**************************Menu de opciones evaluacion**************************")
    print("1- Imprimir una lista de marcas de autos")
    print("2- Realizar una division de dos numeros")
    print("3- Describir que es un algoritmo")
    print("4- Describir que estrutura utilizo para que la maquina decida o tome decisiones")
    print("5- Describir que estructura uso para repetir codigo")
    print("6- Salir del programa")
    print("*******************************************************************************")

    # PASO 2: Pedir al usuario ingrese su opcion

    opcion = int(input("Ingrese su opcion: "))

    # PASO 3: Ejecutar la opcion elegida

    if opcion == 1:

        marcas_de_autos = ["Marcas de autos: Ferrari, Mercedez, Fiát, Chevrolet, Buggati, Delorian, Lamborghini."]

        for marca in marcas_de_autos:
            print(marca)
        
    elif opcion == 2:

        numero1 = input("ingrese el primer numero")
        numero2 = input("ingrese el segundo numero")
        # Profe: Faltan los int a los inputs.
        division = numero1/numero2

        print(f"el resultado de la division de {numero1} y {numero2} es: {division}")

    elif opcion == 3:
        
        print("Un algoritmo es un conjunto de pasos que se usan para resolver un problema")
    
    elif opcion == 4:

        print("La estructura que se utiliza en python para tome las deciciones es con if, elif, else")
    
    elif opcion == 5:

        print("La estrucutura que se utiliza para repetir un codigo en python de manera infinita es con while True")
    
    elif opcion == 6:

        print("Gracias por utilizar nuestro programa")
        break
    
    else:

        print("Opcion Incorrecta")
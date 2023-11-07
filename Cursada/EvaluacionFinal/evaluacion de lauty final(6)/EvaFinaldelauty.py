# FECHA:1
# CURSO:4 2
# ESTUDIANTE: lauty solorzano

# PROBLEMA: Crear un menu de opciones de evaluacion

from typing import NoReturn


while True:
    # PASO 1: Mostrar el menu de opciones
    ("************MENU DE OPCIONES DE EVALUAION**************")
    print("1- Imprimir una lista de marcas deportivas")
    print("2- imprimir una divicion de 2 numeros")
    print("3- Describir que es un ALGORITMO")
    print("4- Describir que estructura utilizo para que la maquina tome decisiones")
    print("5- Describir que estructura uso para repetir el codigo")
    print("6- salir del programa")

    # PASO 2: Pedir al ususario ingrese su opcion
    opcion = int(input("ingrese su opcion"))

    # PASO 3: Ejecutar la opcion elegida

    if  "opcion" == 1: # La variable opcion no lleva comillas.
        marcas_deportivas = ["adidas", "puma", "nike", "reebok"]

        for deportivas in marcas_deportivas:
            print(deportivas) 
    
    elif opcion == 2:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))

        division = num1/num2
        print(f"El resultado de dividir {num1} y {num2} es: {division}")

    elif opcion == 3:
        print("Un algoritmo es un conjunto de intrucciones ordenadas y finitas que se utilizan para resolver un problema o realizar una tarea espesifica")

    elif opcion == 4:
        print("Para que la maquina tome desiciones es if, else y elif")

    elif opcion == 5:
        print("La etiqueta que se utiliza para repetir un codigo es while true")

    elif opcion == 6:
        print("Gracias por utilizar nuestro programa")

    break  # Falta indentación a esta sentencia.


else: 
    ("opcion incorrecta, vuelva a intentarlo") 

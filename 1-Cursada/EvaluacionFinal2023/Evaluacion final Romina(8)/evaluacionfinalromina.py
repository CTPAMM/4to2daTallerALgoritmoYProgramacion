# FECHA:1/11/23
# CURSO:4°2
# ESTUDIANTE:Romina Mamani A.

# PROBLEMA: Crear un menu de opciones de evaluacion 

while True:
    # PASO 1:Mostrar el menu de opciones

    print("**********************menu de opciones**********************************")
    print("1- imprimir una lista de marcas de maquillaje")
    print("2- Realizar una division de 2 numeros") 
    print("3- Describir que es un ALGORITMO")
    print("4- Describir que estrucutura utilizo para que la maquina tome decisines")
    print("5- Describir que estructura uso para repetir codigo")
    print("6- salier del programa")

    # PASO 2: Pedir al usuario que ingrese su opcion

    opcion = int(input("ingrese su opcion"))

    # PASO 3: Ejecutar la opcion elegida

    if opcion == 1:
        marcas_maquillajes = ["mary kay","wanda","maybelline","rimmel","loreal"]
    
        for maquillajes in marcas_maquillajes:
            print(maquillajes)
    
    elif opcion == 2:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: ")) 

        division = num1 / num2

        print(f"El resultado de dividir {num1} y {num2} es: {division}")

    elif opcion == 3:
        print("Un algoritmo es un conjunto de instrucciones ordenadas y finitas que se utilizan para resolver un problema o realizar una tarea especifica")

    elif opcion == 4:
        print("Para que la maquina tome decisiones es if,else y elif")

    elif opcion == 5:
        print("La etiqueta que se utiliza para repetir un codigo es while true")

    elif opcion == 6:
        print("Gracias por utilizar nuestro programa")
        break 

    else:
        print("opcion incorrect,vuelve a intentarlo")



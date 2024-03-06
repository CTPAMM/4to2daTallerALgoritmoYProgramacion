# FECHA: 1/11/23
# CURSO:4/2
# ESTUDIANTE: THIAGO CASTELLANO

#PROBLEMA: crear un menu de opciones de evaluacion.

while True:
    #PASO 1: mostar el menu de opciones.
    print("MENU DE OPCIONES DE evaluacion")

    print("1- imprimir una lista de marca de")
    print("2- realizar una divicion de 2 numeros")
    print("3- describir que es un algoritmo")
    print("4- describir que estrucra utilizo para que la maquina tome decisiones")
    print("5- describir que estrucra uso para repetir codigo")
    print("6- salir del programa")

    # PASO 2: pedir al usuario ingrense su opcion.

    opcion = int(input("ingrese su opcion :"))

 
    # PASO 3: ejecutar la opcion.

    if opcion == 1:
        marcas_empresas = ['samsung','lenovo','juana manso','adidas','motorola','nike']

        for marca in marcas_empresas:
            print(marca)
    
    elif opcion == 2:
        num1 = int(input("ingresr el primer numero"))

        num2 = int(input("ingresar el segundo numero"))

        division = num1 / num1  # Profe: Mal la división.

        print(f"el relsultado de devidir {num1} y {num2} es:{division}")

    elif opcion == 3:
        print("un algoritmo es un conjunto de intrucciones paso a paso para relsolve un problema o realizar una tarea especifica")

    elif opcion == 4:
        print("para que la maquina tome deciones son elif,else,if")

    elif opcion == 5:
         print("la etiqueta que utiliza para repetir un codigo es while True: ")
    
    elif opcion == 6:
        print("gracias por usar mi programacion")
        break
       
    else: 
        print("vuelvalo a intertar mas tarde gracias")



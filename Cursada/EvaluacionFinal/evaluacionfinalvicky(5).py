# FECHA: 1/11/23
# CURSO: 4°2
# ESTUDIANTE: Victoria Pibernus


# PROBLEMA: Crear un menú de opciones de evaluación

while True:
    # PASO 1: Mostrar el menú de opciones.

print("***************************MENU DE OPCIONES*****************************")
print("1- Imprimir una lista de marcas de celulares")
print("2- Realizar una division de 2 números")
print("3- Describir qué es un  algoritmo")
print("4- describir qué estructura utilizo para que la maquina tome decisones")
print("5- Describir qué estructura uso para repetir código")
print("6- Salir del programa")

# Profe: Falta indentar los prints.

   # PASO 2: pedir que ingrese su opción.

   opcion int(input("Ingrese su opcion: "))

   # PASO 3: Ejecutar la opción elegida.

    if opcion == 1: 

        marcas_celulares = ['Samsung', 'Motorola', 'Apple', 'Xiaomi', 'Huawei']

        for marca in marcas_celulares:
            print(marca)

   elif opcion == 2: 
    num1 = int(input("ingrese numero1"))
    num2 = int(input("ingrese numero2"))

    division = num1 / num2
       print(f"el resultado de dividir {num1} y {num2} es: {division}")

  
   elif opcion == 3:
     print("un algoritmo es un conjunto de instrucciones paso a paso para resolver un problema realizado en una tarea específica")

   elif opcion == 4:
     print("para que la maquina tome decisiones son elif, else e if")

   elif opcion == 5:
     print("para repetir el codigo se utiliza la etiqueta wile True")

   elif opcion == 6: 
     print("Gracias por utilizar nuestro programa")
        break
    
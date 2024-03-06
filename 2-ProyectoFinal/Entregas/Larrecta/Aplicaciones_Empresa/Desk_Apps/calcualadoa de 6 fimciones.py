print("******************menu de operaciones********************")
print("1- suma")
print("2- resta")
print("3-multiplicacion")
print("4-division")
print("5-potenciacion")
print("6-raciacion")
print("**********************************************")

opcion = int(input("*ingrese una opcion de operacion: ") )
             
#comienza la logica del programa            
             
print("***********inicia la aplicacion*********************")

numero1 = input("ingrese el primer numero")
numero2 = input("ingrese el segundo numero")

if opcion == 1:
    suma =numero1+numero2
    print(f"el resultado de sumar (numero1) y (numero2) es: (suma)")
    
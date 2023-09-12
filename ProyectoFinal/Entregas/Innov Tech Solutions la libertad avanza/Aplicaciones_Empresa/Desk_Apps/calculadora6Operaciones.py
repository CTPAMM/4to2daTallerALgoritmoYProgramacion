#calculadora para realizar operaciones matematicas (6)
print("**************************************************")
print("bienvenidos a la calculadora de 6 operaciones")
print("**************************************************")


print("*************** Menu*************")
print("1- Logo")
print("2- resta")
print("3-Multiplicacion")
print("4-division")
print("5-potenciacion")
print("6-Radicacion")
print("*********************************")

opcion = int(input("ingrese una opcion de operacion del menu"))

# Comienza la logica del programa

print("************ inicia el programa ************")

numero1 = input("ingrese el primer numero: ")
numero2 = input("ingrese el segundo numero")

if opcion == 1:
    suma= numero1+numero2
    print(f"el resultado de sumar {numero1} y {numero2} es: {suma} ")

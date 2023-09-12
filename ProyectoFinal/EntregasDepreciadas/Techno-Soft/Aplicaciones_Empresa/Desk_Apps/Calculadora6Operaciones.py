# Calculadora para realizar operaciones matemáticas (6)

print("****************************************************************")
print("Bienvenido a la calculadora de 6 operaciones")
print("****************************************************************")

print("********************** MENU DE OPERACIONES **********************")
print("1- SUMA")
print("2- RESTA")
print("3- MULTIPLICACIÓN")
print("4- DIVISIÓN")
print("5- POTENCIACIÓN")
print("6- RADICACIÓN")
print("****************************************************************")

opcion = int(input("Ingrese una opción de operación: "))

# Comienza la lógica del programa.

print("********************** Inicia aplicación **********************")

numero1 = input(" Ingrese el primer número: ")
numero2 = input(" Ingrese el segundo número: ")

if opcion == 1:
    suma = numero1+numero2
    print("El resultado de sumar {numero1} y {numero2} es: {suma}")
elif opcion == 2:
    resta = numero1-numero2
    print(f"El resultado de resta {numero1} y {numero2}")
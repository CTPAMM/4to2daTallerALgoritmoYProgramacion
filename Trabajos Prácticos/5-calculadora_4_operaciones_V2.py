#------------------------------------------------------------------------------------
# Fecha: 10-05-23
# Estudiante: Su Nombre completo
# Título: Calculadora de 4 operaciones V2 (aplicando funciones)
#------------------------------------------------------------------------------------

# Definir las funciones SUMAR-RESTAR-MULTIPLICAR-DIVIDIR

def sumar(a, b):
    return a+b


def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

print("Ingrese los números: ")

num1=float(input("Introduzca el primer número: "))

num2=float(input("Introduzca el segundo número: "))

print("****Menú de opciones*****")
print("1- Sumar")
print("2- Restar")
print("3- Multiplicar")
print("4- Dividir")
print("*************************")

opcion = input("Introduzca su opción: ")

if opcion == "1":
    resultado = sumar(num1, num2)
    print(f"el resultado de la suma es: {resultado}") 
    
if opcion == "2":
    resultado = restar(num1, num2)
    print(f"el resultado de la resta es: {resultado}") 
    

if opcion == "3":
    resultado = multiplicar(num1, num2)
    print(f"el resultado de la multiplicación es: {resultado}") 
    
if opcion == "4":
    resultado = dividir(num1, num2)
    print(f"el resultado de la división es: {resultado}") 


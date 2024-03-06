# Evaluacion del 03/05/2023
# Abigail Rejala
# 4°2

# 1° Programa
# Imprima en pantalla un menu de 4 opciones a eleccion.

print("****Menu de opciones*****")
print("1- caramelos")
print("2- chupetines")
print("3- chicles")
print("4- gomitas")
print("*************************")

# 2° Programa 
# Ingrese por teclado 2 numeros e imprima en pantalla el resultado de la multiplicación

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print(f"La multiplicacion de los numeros es: ")
print(numero1 * numero2)

# 3° Programa
# Crear una lista con 4 elementos e imprimirla en pantalla

lista_golosinas = {'caramelos, chupetines, "chicles, gomitas"'}

print(lista_golosinas)

for golosina in  lista_golosinas: 
    print(golosina)

# 4° Programa
# Crear una calculadora de perimetro del rectangulo 

#Declaro y defino las variables
base = int(input("Introduzca el tamaño de la base: "))
altura = int(input("Introduzca el tamaño de la altura: "))

# Calculo la perimetro del cuadrado
respuesta = (base*2) + (altura*2) 

#Muestro la respuesta 
print("La superficie del rectangulo es: ")
print(respuesta)
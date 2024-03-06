# Evaluación del 03/05/2023
# Mariana Luna Cabaña
# 4°2°

# 1° Programa
# Imprima en pantalla un menú de 4 opciones a elección.

print("***Menú de Songs***")
print("1- Tous le memes")
print("2- Goo Goo Muck")
print("3- Yad")
print("4- Sun Down, I'm Up")
print("**********************")

# 2° Programa
# Ingrese por teclado 2 números e imprima en pantalla el resultado 
# de la multiplicación de ambos.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("La multiplicación de los números es: ")
print(numero1 * numero2)

# 3° Programa
# Crear una lista de 4 elementos e imprimirla en pantalla.

equipos_futbol = ["River, Boca, Racing, Velez"]

print(equipos_futbol)

for equipos in equipos_futbol:
    print(equipos)
    
# 4° Programa
# Crear una calculadora de perímetros de rectángulos.

base = int(input("Introduzca el tamaño de la base: "))
altura = int(input("Introduzca el tamaño de la altura: "))

# Calculo la superficie del rectángulo
respuesta = (base * 2) + (altura * 2)

# Muestro la respuesta
print("El perímetro del rectángulo es: ")
print(respuesta)




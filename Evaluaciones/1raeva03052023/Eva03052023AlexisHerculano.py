# Evaluacion del 03/05/2023
# Alexis Valentin Herculano Maidana Venegas Gomez
# 4° 2°

# 1° Programa
# Imprima en pantalla un menu de cuatro opciones a eleccion

print("-----Menu de opciones de Leyendas Argentinas-----")
print("1-Messi")
print("2-Maradona")
print("3-DI Stefano")
print("4-Kempes")
print("-------------------------------------------------")

# 2° Programa
# Ingrese por teclado 2 numeros e imprima el resultado de el resultado de multiplicacion de ambos


numero_1 = float(input("Introduce el valor del primer numero: "))
numero_2 = float(input("Introduca el valor de segundo numero: "))

print(numero_1 * numero_2)

# 3° Programa
# Crear Una Lista de 4 elementos e imprimirla en pantalla

los_Mejores_De_La_Historia = ['Messi', 'Maradona', 'Ronaldo', 'Pele']

for leyendas in los_Mejores_De_La_Historia:
    print(leyendas)

# 4° Programa
# Crear una calculadora de erimetros de retangulos

Lado = None

# Calculo la superficie de cuadrado
print("Calculadora de superficies de rectangulo")

base = float(input("Introdusca el tamaño de base: "))
altura = int(input("Introdusca el tamaño del altura: "))

#  Calculo de la superficie 

respuesta = base *2 + altura *2

# Muestro la respuesta
print("La superficie del rectangulo es: ")
print(respuesta)
#Evaluación del 03/05/2023
#Estudiante: Noelia Escobar
#Curso: 4°2°

# 1° Programa 
# Imprima en pantalla un menú de 4 opciones a eleccion 

print("         Menú de videojuegos         ")
print("                         ")
print("1- Zelda")
print("2- Super Mario kart")
print("3- Minecraft")
print("4- GTA5")
print("                         ")

# 2° Programa
# ingrese por teclado 2 numeros e imprima en pantalla el resultado de su Multiplicacion(*)

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("         ")
print(" La Multiplicacon de los numeros es:      ")
print(numero1 * numero2)
print("                                     ")

# 3° Programa 
#Crear una lista con 4 elementos e imprimala en pantalla

print("         Lista de Zapatillas         ")
print("                                     ")

lista_Marcas_de_zapatillas = ("     Nike'; Jordan'; Addidas'; Vans'")

print(lista_Marcas_de_zapatillas)
print("                                      ")
print("         Calculadora de perimetro            ")
print("                                         ")

# 4° Programa
#Crear una calculadora de perimetro del rectangulo

print("calculadora de perimetro de rectangulos\n")

#Declaracion y definicion de variables.
base= int(input("introduzca el temaño de la base: "))
altura = int(input("introduzca el tamaño de la altura: "))

#Calculo la superficie del rectangulo
respuesta = base*2 + altura*2

#Muestro la respuesta
print("El perimetro del rectangulo es: ")
print(respuesta)
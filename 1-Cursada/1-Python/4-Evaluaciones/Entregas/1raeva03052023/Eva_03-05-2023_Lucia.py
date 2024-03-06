# ---------------------------------------------
# Evaluacion del 03/05/2023
# Nombre Completo: Angela Lucia Quispe
# Curso: 4to 2da
#----------------------------------------------

# 1er Programa
# Imprima en pantalla un menu de 4 opciones a eleccion

print("****Menu de Comidas*****")
print("1- Pizza")
print("2- Pancho")
print("3- Hamburguesa")
print("4- Sopa")
print("************************")

# 2do Programa
# Ingrese por tecladd dos numeros e imprima en pantalla
# resltado de la multiplicacion de ambos.

numero1 =int(input("Ingrese el primer numero: "))
numero2 =int(input("Ingrese el segundo numero: "))

print("La multiplicacion de los numeros es:")
print(numero1 * numero2)

# 3er Programa
# Crear una lista e imprimir en pantalla

lista_deportes = ['Futbol','Voley', 'Basket', 'Handball']

print( lista_deportes )

for deporte in lista_deportes:
    print(deporte)

# 4to Programa
# Crear una calculadora de perimetro del rectangulo.

# Declaro y defino las variables.
base= int(input("Introduzca el tamaño de la base: "))
altura = int(input("Introduzca el tamaño de la altura: "))

# Calculo la superficie del rectangulo.
respuesta = ( base * 2) + ( altura * 2)

# Muestro la respuesta
print("El perimetro del rectangulo es: ")
print(respuesta)
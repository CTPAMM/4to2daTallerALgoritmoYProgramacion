# -------------------------------------------------------------------------------
# Fecha: 05-07-23
# Curso: 4° 2°
# Estudiante: Lautaro solorzano 
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print("Hello world")

'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''
numero1 = 3
numero2 = 5

print("La suma de los numeros es: ")
print(numero1 + numero2)

'''    
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''
primerNombre = input("Ingrese el primerNombre: ")
segundoNombre = input("Ingrese el segundoNombre: ")
apellido = input("Ingrese el apellido")

input(f"Hola {primerNombre} {segundoNombre} {apellido}") 

'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

print("La multiplicacion de los numeros es: ")
print(numero1 . numero2 . numero3)

'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
if numero2 > numero3:
    print(f"El {numero3} es el mayor")
'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''
numero3 = int(input("Introduzca el primer numero: "))

if numero3 % 2:
    print(f"El numero {numero3} es divisivle por 2")
else:
    print(f"El numero {numero3} no es divisivle por 2")

'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
'''
numero1= int(input("Introduzca el primer numero: "))

if numero1 % 2 and numero1 % 3: 
    print(f"El numero {numero1} es divisivle por 2")
else:
    print(f"El numero {numero1} no es divisible por 3")
'''
8) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
'''
nota = int(input("Introduzca la nota: "))

if nota > 0 and nota <= 3:
    print("Muy deficiente")
elif nota > 3 and nota <= 5:
    print("Insuficiente")
elif nota > 5 and nota <= 6:
    print("Suficiente")
elif nota > 6 and nota <= 7:
    print("Bien")
elif nota > 7 and nota <= 9:
    print ("Notable")
elif nota > 9 and nota <= 10: 
    print("Sobresaliente")
'''
9) Crea una lista llamada lista_numeros y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33
'''
lista_numero = [10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33]

'''
   a) Imprime el valor menor y mayor.
'''
print(f"El mayor numero es {lista_numero[2]} y el menor numero {lista_numero[9]}")

'''
   b) Imprime la lista ordenada de menor a mayor
'''
lista_numero.sort()

print(lista_numero) 

'''
   c) Imprime el largo de la lista
'''
print(len(lista_numero))

'''
   d) Imprime cuantas veces se repite el número 10
'''
print(lista_numero.count(10))

'''
10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo
'''
lista_colores = ["rojo","azul", "verde","amarrillo"]

'''
    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
'''
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3, "naranja")

print(lista_colores) 
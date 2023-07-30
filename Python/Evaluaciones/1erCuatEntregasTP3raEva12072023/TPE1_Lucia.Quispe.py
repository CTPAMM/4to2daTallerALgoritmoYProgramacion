# -------------------------------------------------------------------------------
# Fecha: 28-06-23
# Curso: 4° 2°
# Estudiante: Su nombre completo 
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
''''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print("Hello World")

'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''
numero_1 = 3
numero_2 = 5

print(numero_1 + numero_2 )
'''
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''
primer_nombre = input(" Introduzca su primer nombre: ")
segumdo_nombre = input(" Introduzca su segundo nombre: ")
Apellido = input(" Introduzca su Apellido")

print(f"hola {primer_nombre} {segumdo_nombre} {Apellido}")

'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero_1 = float(input("Introduzca el valor del primer numero: "))
numero_2 = float(input("Introduzca el valor del segundo numero: "))

print(numero_1 * numero_2)
print("La multiṕlicacion de ambos números es igual a: ");

'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
numero_1 = float(input("Introduzca el valor del primer numero: "))
numero_2 = float(input("Introduzca el valor del segundo numero: "))

if numero_1 > numero_2:
    print(f' El {numero_2} es el mayor')
else:
    print(f'El {numero_1} es el mayor')

'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''
numero_1 = float(input("Introduzca un numero: "))
if numero_1 % 2:
    print(f'El {numero_1} es divisible por 2' )

else:
     print(f'El {numero_1} no es divisible por 2' )

'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
(sólo hay que comprobar si lo es por uno de los cuatro)
'''
numero_1 = float(input("Introduzca un numero: "))

if numero_1 % 2 and numero_1 % 3:
    print(f'El {numero_1} es divisible por 2 y por 3' )

else: 
     print(f'El {numero_1} no es divisible por 2 ni por 3')

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

if nota > 0 and nota < 3:
    print("Muy deficiente")

elif nota > 3 and nota <5:
    print("Insuficiente")

elif nota > 5 and nota <6:
    print("Suficiente")

elif nota > 6 and nota <7:
    print("Bien")

elif nota > 7 and nota < 9:
    print("Notable")

elif nota > 9 and nota <10:
    print("Sobresaliente")

'''
9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33
'''
lista_numeros = ['10','45', '356', '50','10','15','46','67','45','5','28','43','10','65','10','33']
'''
   a) Imprime el valor menor y mayor.
'''
print(f'El valor menor numero es {lista_numeros[9]} y el mayor numero es{lista_numeros[2]}')
'''
   b) Imprime la lista ordenada de menor a mayor
'''
lista_numeros.sort()

print(lista_numeros)
'''
   c) Imprime el largo de la lista
'''
print(len(lista_numeros))
'''
   d) Imprime cuantas veces se repite el número 10
'''
print(lista_numeros.count[10])
'''
10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo
'''
lista_colores = ["rojo","azul","verde","amarillo"]
'''
    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
        gris - Antes de "rojo".
        rosa - En último lugar.
        naranja - Entre "azul" y "verde".
'''
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")

print(lista_colores)
# -------------------------------------------------------------------------------
# Fecha: 05-07-23
# Curso: 4° 2°
# Estudiante: Mariana Cabaña
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print("Hello  World")
'''

2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''
numero_1 = 3
numero_2 = 5

print("La suma de 3+5 es igual a: ")
print(numero_1 + numero_2)
'''

3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''
primernombre = (input("Ingrese el primer nombre: "))
segundonombre = (input("Ingrese el segundo nombre: "))
apellido = (input("Ingrese el apellido: "))

print(f"Hola {primernombre} {segundonombre} {apellido}")
'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("La multiplicación de los números es: ")
print(numero1 * numero2)
'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
primerNumero = int(input("Ingrese el primer número: "))
segundoNumero = int(input("Ingrese el segundo número: "))

if primerNumero > segundoNumero:
    print("el número mayor es: {primerNumero}")
else:
    print("el número mayor es: {segundoNumero}")
'''

6) Escribe un programa que pida un número y diga si es divisible por 2
'''
numero = int(input("Ingrese el número: "))

if numero % 2:
    print(f"El número {numero} es divisible por 2")
else:
    print(f"Este numero no es divisible por 2")    
'''

7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3
'''
numero = int(input("Ingrese el número: "))

if numero%2 == 0 and numero%3 == 0:
    print(f"El número {numero} es divisible por 2 y por 3")
else:
    print(f"Este numero no es divisible por por 2 y por 3")
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
    print("Insufuciente")
elif nota > 5 and nota <= 6:
    print("Sufuciente")
elif nota > 6 and nota <= 7:
    print("Bien")
elif nota > 7 and nota <= 9:
    print("Notable")
elif nota > 9 and nota <= 10:
    print("Sobresaliente")
'''

9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33
'''
lista_numero = [10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33]
'''

   a) Imprime el valor menor y mayor.
'''
print(f"El mayor numero es {lista_numero[2]} y el menor número {lista_numero[9]}")
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
lista_colores = ["rojo", "azul", "verde", "amarillo"]
'''

    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
        gris - Antes de "rojo".
        rosa - En último lugar.
        naranja - Entre "azul" y "verde".
'''
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3, "naranja")

print (lista_colores)

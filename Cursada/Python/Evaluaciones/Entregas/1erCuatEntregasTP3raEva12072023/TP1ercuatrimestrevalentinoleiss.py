# -------------------------------------------------------------------------------
# Fecha: 28-06-23
# Curso: 4° 2°
# Estudiante: Valentino Leiss
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''
print("hello world")
'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''
numero1 = 3
numero2 = 5
resultado = numero1+numero2 
print(f"la suma de 3 + 5 es: {resultado}")

'''
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''
primernombre = input("introduzca su primer nombre: ")
apellido = input("introduzca su apellido: ")
print(f"hola {primernombre} {apellido}")
'''
4) Escribe un programa que pida un número, pida otro número y escriba el resultado de multiplicar estos dos números.
'''
numero1 = int(input("introduzca el primer numero: "))
numero2 = int(input("introduzca el segundo numero: "))

resultado = numero1 * numero2

print(f"la multiplicacion de {numero1} y {numero2} es: {resultado}")
'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
numero1 = int(input("introduzca el primer numero: "))
numero2 = int(input("introduzca el segundo numero: "))
              
if numero1 > numero2:
    print(f"el numero{numero1} es mayor")
else:
    print(f"el numero {numero2} es mayor")
'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''
numero1 = int(input("introduzca el primer numero: "))
numero2 = int(input("introduzca el segundo numero: "))
if numero1 % 2:
    print(f"el numero{numero1} es divisible por 2")
else:
    print(f"el numero {numero2} es divisible por 2")

'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
(sólo hay que comprobar si lo es por uno de los cuatro)
'''
numero1 = int(input("introduzca el primer numero: "))
numero2 = int(input("introduzca el segundo numero: "))
if numero1 % 2 and 3:
    print(f"el numero{numero1} es divisible por 2 y 3")
else:
    print(f"el numero {numero2} es divisible por 2 y 3")
'''
8) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
'''
nota=int(input("introduzca la nota: "))

if nota > 0 and nota <= 3: 
    print("muy deficiente")
elif nota > 3 and nota <= 5:
    print("insuficiente") 
elif nota > 5 and nota <= 6: 
    print("suficiente")
elif nota > 6 and nota <= 7:
    print("bien")
elif nota > 7 and nota <= 9:
    print("notable")
elif nota > 9 and nota <= 10:
    print("sobresaliente")
  
'''
9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33

   a) Imprime el valor menor y mayor.
   b) Imprime la lista ordenada de menor a mayor
   c) Imprime el largo de la lista
   d) Imprime cuantas veces se repite el número 10
'''
lista_numero= [10,45,356,50,10,15,46,67,45,5,28,43,10,65,10,33]

# a)
 
print(f"el mayor numero es {lista_numero[2]} y el menor número {lista_numero[9]}")

# b)
print(f"5,10,10,10,10,15,28,33,43,45,45,46,50,65,67,356")

# c)
print(len(lista_numero))

# d)
print(lista_numero.count(10))
'''
10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo

    a) Imprime la lista modificada luego de añadir los colores en el código en este orden:
        gris - Antes de "rojo".
        rosa - En último lugar.
        naranja - Entre "azul" y "verde".
'''
lista_colores = ["rojo,azul,verde,amarillo"]

#a)
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")

print(lista_colores)
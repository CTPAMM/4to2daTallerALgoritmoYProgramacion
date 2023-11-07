# -------------------------------------------------------------------------------
# Fecha: 28-06-23
# Curso: 4° 2°
# Estudiante: Su nombre completo 
# Título: Trabajo Práctico Evaluativo del 1er Cuatrimestre
#--------------------------------------------------------------------------------
'''
1) Escribe un programa muestre por pantalla “Hello World”.
'''

print("hello world")   

'''
2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
'''

numero1 =3
numero2 =5

resultado  = numero1 + numero2

print(" la suma de 3 + 5 es {resultado}")

'''
3) Escribe un programa que pida el primer nombre, segundo nombre y apellido y escriba un texto que diga “Hola nombre completo”
'''

primerNombre = input("intruduzca su primer thiago: ")
segundoNombre = input("introduzca su segundo uriel") 
apellido = input("introduzca su apellido castellano")   

print(f"thiago") 

print(f"uriel")

print(f"castellano")



''''
4) Escribe un programa que pida un número", pida otro número y escriba el resultado de multiplicar estos dos números.
'''



numero1 = int(input("introduzca el primer numero: "))

numero2 = int(input("introduzca el segundo numero: "))

resultado = numero1 * numero2

print(f"la multiplicacion del {numero1} * {numero2} es {resultado}")




'''
5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''

numero1 = int(input("introduzca el primer numero: "))

numero2 = int(input("introduzca el primer numero: "))

if numero1 > numero2:
    print(f"el numero1 {numero2}es mayor es {numero1} ")
else:
    print(f"el {numero1} es mayor que el {numero2}")


'''
6) Escribe un programa que pida un número y diga si es divisible por 2
'''



numero1 = int(input("introduzca el primer numero: ")

if numero1 % 2:
 print(f"el numero {numero1}es divisible por 2 ")


else:
print("el {numero1}no es divisible por 2")


'''
7) Escribe un programa que pida un número y nos diga si es divisible por 2 y 3 
(sólo hay que comprobar si lo es por uno de los cuatro)
'''




numero1 = int(input("introduzca el primer numero: "))

if numero1 % 2 % 3:
    print(f"el numero {numero1}es divisible por 2 y 3 ")


else:
print(f"el numero {numero1}no es divisible por 2 o 3")



'''
8) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente
'''
nota = int(input("introduzca la nota:"))

if nota > 0 and nota <= 3:
    print("MUY deficiente")
 elif nota >3 and nota <= 5:
    print("muy insuficiente")
elif nota > 5 and nota <= 6:
    print("suficiente")
elif nota >6 and nota <=7:
    print("bien")
elif nota >7 and nota <=9:
    print("notable")
elif nota >9 and nota <=10:
    print("sobresaliente")
    
'''

9) Crea una lista llamada "lista_numeros" y almacena los siguientes valores integer:
10,45,356,50,10,15,46,67,45,10,28,43,10,65,10,33

   a) Imprime el valor menor y mayor.
   '''
print(" el mayor numero es {lista_numero[356]} y el memor numero {lista_numero[5]}")

   '''
   b) Imprime la lista ordenada de menor a mayor
   '''

lista_numero.sort()
print(lista_numero)

   '''
   c) Imprime el largo de la lista
   '''
print(len(liista_numero))


   '''
   d) Imprime cuantas veces se repite el número 10
   '''
print(lista_de numero.count(10))
   '''

10) Crea una lista llamada "lista_colores" y almacena los siguientes valores string:
rojo, azul, verde, amarillo
 '''
lista_colores = ["rojo",azul,verde,amarillo]

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

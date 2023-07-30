# Evaluación del 03/05/2023
# Victoria Pibernus
# 4° 2° 

# 1° Programa
# Imprima en pantalla un menú de 4 opciones a elección.

print(***menú celulares***)
print("1- Samsung")
print("2- Iphone")
print("3- Motorola")
print("4- Huawei")

# 2° Programa
# Ingrese por teclado 2 números e imprima  en pantalla el 
# resultado de la multiplicación de ambos.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("La multiplicación de los números es: ")
print(numero1 * numero2)


# 3° Programa
# Crear una lista de elementos e imprimirla en pantalla.
 
lista_maquillaje = ['Labial', 'Delineador', 'Rimel', "Rubor"]

print(lista_maquillaje)

# Bucle for
for lenguaje in lista_maquillaje:
    print(lenguaje)

# 4° Programa
# Crear una calculadora de perimetros de rectángulos

#declaro y defino las variables
base = int(input("Introduzca el tamaño de la base: "))
altura = int(input("Introduzca el tamaño de la altura: "))

# Calculo de perimetro del rectangulo
respuesta = (base*2 + altura*2)

# Muestro la respuestas
print("el perimetro del rectangulo es: ")
print (respuesta)

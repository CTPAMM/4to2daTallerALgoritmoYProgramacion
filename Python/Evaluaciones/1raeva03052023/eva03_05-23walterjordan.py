#evaluacion del 03/05/23
#nombre completo:walter mateo jordan
#4-2


#primer programa 
#imprima en pantalla un menu de cuatro opciones a eleccion


print ("-----menu-----")
print ("------bugati chyron------")
print ("chevrolet corvette")
print ("------- volsvagen poloox--------")
print ("------------toyota supra------")


#ingrise por teclado 2 numeros e imprima en pantalla el resultado de su multiplicacion

numero_1 = 10
numero_2 = 20

print(numero_1 * numero_2)


#3 programa
#crear una lista de elementos e imprimirla en pantalla 
lista_autos = ['clase A',  'hylux', 'corvette', ' Polo']

print(lista_autos)

for auto in lista_autos:
    print(auto)


#4 programa
#crear una calculadora de perimetro de rectangulos

print ("calculadora de superficies del cuadrado")

base= float(input("introduzca el tamaño del base"))
altura = int(input("introduzca el tamaño del altura"))
#calculo de la superficie

respuesta = (base*2) + (altura*2)

#Muestro la resupuesta
print("el perimetro del rectangulo es ")

print(respuesta)

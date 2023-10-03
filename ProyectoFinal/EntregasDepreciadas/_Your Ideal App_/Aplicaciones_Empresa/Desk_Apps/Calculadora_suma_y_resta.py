# PROBLEMA: Un usuario necesita calcular la SUMA y la RESTA de dos números.
# SOLUCIÓN: Crear un algoritmoque solucionela suma y la resta

# PASO 1: Pedir al usuario que ingrese los números a operar.

numero_1 = float(input("Introduzca el valor del primer numero: "))
numero_2 = float(input("Introduzca el valor del segundo numero: "))

# PASO 2: Mostrar el menú de opciones.

print("¿Qué operacion desea realizar? ");

# Presentar menu de opciones:

print("1- Sumar");
print("2- Restar"); 

# PASO 3: Pedir al usuario ingresar la opción que eligida 

opción = input("Ingrese su opción: ");

# PASO 4: Realizar la operación seleccionada por el usuario.

if opción =="1":
    print("La suma de ambos numeros es igual a: ")
    print(numero_1 + numero_2)

elif opción =="2":
    print("La resta de ambos numeros es igual a: ");
    print(numero_1 - numero_2)
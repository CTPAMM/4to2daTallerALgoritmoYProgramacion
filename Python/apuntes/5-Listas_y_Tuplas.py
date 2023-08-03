#----------------------------------------------------------
# Fecha: 02-08-23
# Estudiante: Su Nombre Completo
# Título: Listas y Tuplas.
#----------------------------------------------------------

#---------------------------------------------------------------------
#  LISTAS
#---------------------------------------------------------------------
# Declarar y definir las variables
lista_marcas = ['vw', 'Pagani', 'Mitshubishi', 'Lexus']
print(lista_marcas) 

# Imprimir la lista con un bucle FOR
for marca in lista_marcas:
    print(marca)
    
# Imprimir un elemento concreto de la lista
print(f"La marca es: {lista_marcas[2]}")

# Reemplazar un elemento de la lista
lista_marcas[2] = 'Toyota'
print(lista_marcas)

# Agregar un elemento en la lista en la última posición
lista_marcas.append('Fiat')
print(lista_marcas)

# Agregar un elemento en la lista en una posición concreta
lista_marcas.insert(3, 'DS')
print(lista_marcas)

# Eliminar un elemento concreto de la lista
lista_marcas.pop(0)
print(lista_marcas)


# Este es el comienzo del segundo semestre en Laboratorio II
# Colecciones en python

## Colecciones | 16-08-2022

# Listas
# Son un conjunto de elementos
# lista = Ariel, Liliana, Natalia, Osvaldo
# indice    0       1        2        3

nombres = ['Natalia', 'Osvaldo', 'Liliana', 'Ariel'] # Lista

# Dentro de una misma lista puede haber distintos tipos de elementos

print(nombres) # Imprime la lista 'nombres'
print(nombres[0]) # Imprime el 'primer' elemento de la lista 'nombres'
print(nombres[3]) # Imprime el 'cuarto' elemento de la lista 'nombres'

print(nombres[-1]) # Imprime el 'último' elemento de la lista 'nombres'
print(nombres[-2]) # Imprime el 'penúltimo' elemento de la lista 'nombres'

print(nombres[0:2]) # Imprime las primeras dos posiciones, indice 0, 1 pero no el 2

# Ir desde el comienzo de la lista al indici (sin incluirlo)
print(nombres[ :3]) # Muestra desde el indice '0' hasta la 3ra posición, indice '2'
# Desde el indice indicado hasta el final
print(nombres[1: ]) #Muestra desde el indice '1' hasta la última posición

# Modificamos un valor
nombres[3] = 'Agustín'
nombres[0] = 'Nicolas'
print(nombres)

# Iterar una lista
for nombre in nombres: # Por cada elemento(nombre) en la lista 'nombres' imprimir
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Retornamos la cantidad de elementos en una lista
print(len(nombres))

# Agregamos un elemento a la lista
nombres.append('Jorge')
print(nombres)

# Insertamos un elemento a la lista en un indice especifico
nombres.insert(1, 'Gabriel')
print(nombres)
nombres.insert(3, 'Cintia')
print(nombres)

# Eliminamos un elemento de la lista
nombres.remove('Osvaldo')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un elemento con un indice especifico
del nombres[2]
print(nombres)

# Eliminar todos los elementos de una lista
nombres.clear()
print(nombres)

# Eliminar 'la lista'
del nombres

# Tuplas
# Definir una tupla

cocina = ('cuchillo', 'cuchara', 'tenedor')
print(len(cocina))

# Acceder a un elemento de una tupla
print(cocina[0])
# Al revés (desde el último al primero)
print(cocina[-1])

# Acceder a un rango de elementos en una tupla
print(cocina[0:1])

# ACLARACIÓN: Se necesita una coma para hacer una tupla, de lo contrario es un str
verdura = ('papa',) #<--- es una tupla gracias a la coma

# Recorremos una tupla
for cocinar in cocina:
    print(cocinar, end=' ') # Finaliza con un espacio y se ve en una sola línea

# ACLARACIÓN: Una tupla nunca se puede modificar
#cocina[0] = 'plato'
#print(cocina) # Esto es un error, como deja ver la terminal

# Realizamos una conversión de 'tupla' a 'lista'
# ACLARACIÓN: Es una mala práctica
cocinaLista = list(cocina) # tuple -> list
cocinaLista[0] = 'plato'

cocina = tuple(cocinaLista) # list -> tuple
print('\n', cocina)

# Eliminar una tupla
del cocina
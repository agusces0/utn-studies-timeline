# Este es el comienzo del segundo semestre en Laboratorio II
# Colecciones en python

## Colecciones parte 1 | 16-08-2022

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

## Colecciones parte 2 | 23-08-2022

# Tipo SET
# ACLARACIÓN: SET no tiene indices, ni se puede editar
planetas = {'Tierra', 'Marte', 'Venus', 'Saturno'}
print(planetas)
print(len(planetas))

# Revisar si un elemento se encuentra dentro de SET. (También se puede hacer en list & tuple)
print('Marte' in planetas)
# Revisar si un elemento NO se encuentra dentro de SET
print('Tierra' not in planetas)

# Agregamos un elemento a SET
# ACLARACIÓN: Por más que se agregue un elemento igual a otro, no se duplica
planetas.add('Neptuno')
print(planetas)

# Eliminar un elemento de SET
planetas.remove('Venus')
print(planetas)
planetas.discard('Tierra') # NO da error al 'no encontrar' el elemento en SET
print(planetas)

# Limpiar SET
planetas.clear()
print(planetas)

# Eliminar SET
del planetas

# Diccionario
# Un diccionario esta compuesto por una palabra clave y una descripción
# dict(key, value)

diccionario = {
    'IDE':'Integrated Develompent Enviroment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con una palabra clave
print(diccionario['IDE'])
print(diccionario.get('POO'))

# Modificamos elementos de un diccionario
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario['IDE'])

# Recorrer los elementos de un diccionario
for key in diccionario: # De esta manera solo se recorren las KEY
    print(key)

# Es necesaria una función para recorrer el diccionario
for key, value in diccionario.items():
    print (key, value)

# Otras formas de recorrer un diccionario
for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)

# Comprobar si un elemento se encuentra en el diccionario
print('IDE' in diccionario)
print('IDE' not in diccionario)

# Agregar un elemento en el diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento del diccionario
diccionario.pop('SABD')
print(diccionario)

# Vaciar un dict
diccionario.clear()
print(diccionario)

# Borrar un diccionario
del diccionario

# Concatenación de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9]) # Función para agregar multiples elementos
lista3.extend([1, 1, 1]) #En total hay 4 1
print(lista3)

print(lista3.index(5)) # Función para averiguar el index de un elemento

# Como saber cuantos 'elementos repetidos' hay dentro de una lista
print(lista3.count(1))

# Para poner al revés una lista
lista3.reverse()
print(lista3)

# Para que una lista repita sus elementos
lista = [1,2,3] * 2 # Se repite, no se multiplican
print(lista)

# Métodos de ordenamiento
lista3.sort() # Ordena de menor a mayor
print(lista3)
lista3.sort(reverse=True) # Ordena de mayor a menor
print(lista3)

# Repaso tupla
tupla = (4, 'Hola', 6.78, [1, 2, 78], 'Hola') # Puede tener multiples elementos dentro
print(tupla)

print(4 in tupla)
print(4 not in tupla)

## Colecciones parte 3 | 30-08-2022

# Repaso set o conjunto
conjunto2 = set()
conjunto1 = {'bye', 'Hola'} # ACLARACIÓN: Se encuentra inicializado por las {} y no puede agregarse elementos
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
print(3 not in conjunto1)

# Igualdad de dos set o conjuntos
print(conjunto1 == conjunto2) # Devuelve bool

# Operaciones en set o conjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 -  conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Solo muestra elementos NO compartidos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Verificamos si un conjunto es un subconjunto en otro
print(conjunto2.issubset(conjunto3))

print(conjunto3.issuperset(conjunto1)) # Verificamos si los elementos del 1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quere decir que es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en común?

# Convertir un conjunto totalemente en inmutable
conjunto1 = frozenset # <- No se puede agregar, modificar ni eliminar elementos

# Repaso diccionarios
diccionario1 = {'Azul':'Blue', 'Rojo':'Red', 'Verde':'Green', 'Amarillo':'Yellow'}
print(diccionario1)

# Eliminar de un diccionario
del (diccionario1['Azul'])
print(diccionario1)

# los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel':{'Edad':40, 'Altura':1.83}, 'Osvaldo':[45, 1.85], 'Natalia':[35,1.67]}
for key, value in diccionario2.items():
    print(key, value)

# Método con listas llamado PILAS
# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
print(pila)

# Guardar un elemento borrado
elementoBorrado = pila.pop()
print(f'Sacamos el elemento: ', elementoBorrado)
print(f'La pila ahora quedó así: ', pila)

# Método con listas llamado COLA
# Colas con listas
# Estructura de datos de tipo fifo(first input / firt output)

cola = ['Agustín', 'Ana', 'Micaela', 'Valentín']

# Agregamos elementos al final de la cola
cola.append('Lucas')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido: ', seRetira)
print(cola)
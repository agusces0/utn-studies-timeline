# Archivo dedicado a la resolución de ejercicios varios
# Laboratiorio 2 - Python

## Clase 1 - Colecciones | 16-08-2022

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir número divisibles entre 3
# Ejemplo de ejecicion 0,3,6,9

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista1:
    if i%3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de números de 2 a 6 y imprimirlos
# Ejemplo de ejecución: 2,3,4,5,6

print(lista1[2:7])

# Ejercicio 3: Crear un rango de 3 a 10, pero con incremento de 2 en 2, en ligar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9

x = range(3, 10, 2)
for n in x:
  print(n)

# Ejercicio 4: dada la siguiente tupla:
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]

lista2 = list(tupla)
for i in lista2:
    if i < 5:
        print(i)
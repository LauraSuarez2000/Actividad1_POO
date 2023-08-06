#Crear un programa que calcule la suma de los números en una lista dada.

def calcular_suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista_numeros = [2, 4, 6, 8, 10]
suma_total = calcular_suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)

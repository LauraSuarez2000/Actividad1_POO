import random

def generar_lista_numeros_aleatorios(cantidad):
    lista_aleatoria = [random.randint(1, 100) for _ in range(cantidad)]
    return lista_aleatoria

# Generar una lista de 10 números aleatorios
lista_numeros_aleatorios = generar_lista_numeros_aleatorios(10)

# Imprimir la lista en pantalla
print("Lista de números aleatorios:")
print(lista_numeros_aleatorios)

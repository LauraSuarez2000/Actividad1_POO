def encontrar_maximo_minimo(lista):
    if not lista:
        return None, None

    maximo = minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo

# Ejemplo de uso de la función
lista_numeros = [5, 2, 10, 3, 7, 1]
maximo, minimo = encontrar_maximo_minimo(lista_numeros)

print("El número más grande en la lista es:", maximo)
print("El número más pequeño en la lista es:", minimo)

def calcular_media_aritmetica(lista):
    if not lista:
        return None

    suma_total = sum(lista)
    cantidad_numeros = len(lista)
    media = suma_total / cantidad_numeros
    return media

# Ejemplo de uso de la función
lista_numeros = [10, 20, 30, 40, 50]
media_aritmetica = calcular_media_aritmetica(lista_numeros)

print("La media aritmética de la lista es:", media_aritmetica)

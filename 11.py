def generar_lista_pares():
    lista_pares = [num for num in range(2, 101) if num % 2 == 0]
    return lista_pares

# Generar la lista de números pares
lista_pares_generada = generar_lista_pares()

# Imprimir la lista en pantalla
print("Lista de números pares entre 1 y 100:")
print(lista_pares_generada)

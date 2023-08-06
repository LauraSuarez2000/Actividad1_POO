def es_palindromo(cadena):
    # Eliminamos los espacios y convertimos todo a minúsculas
    cadena = cadena.replace(" ", "").lower()

    # Verificamos si la cadena es igual a su versión invertida
    return cadena == cadena[::-1]

# Ejemplo de uso del programa
cadena_ingresada = input("Ingresa una cadena de texto: ")

if es_palindromo(cadena_ingresada):
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")

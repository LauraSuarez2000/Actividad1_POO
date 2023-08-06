def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Ejemplo de uso de la función
numero_ingresado = int(input("Ingresa un número entero para calcular su factorial: "))
resultado = factorial_recursivo(numero_ingresado)
print("El factorial de {} es: {}".format(numero_ingresado, resultado))

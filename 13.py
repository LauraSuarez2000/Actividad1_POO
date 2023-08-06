def calcular_suma(numero1, numero2):
    return numero1 + numero2

def calcular_resta(numero1, numero2):
    return numero1 - numero2

def calcular_multiplicacion(numero1, numero2):
    return numero1 * numero2

def calcular_division(numero1, numero2):
    if numero2 == 0:
        return "Error: No se puede dividir entre cero."
    return numero1 / numero2

# Solicitar al usuario ingresar dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Calcular y mostrar los resultados
print("Suma:", calcular_suma(numero1, numero2))
print("Resta:", calcular_resta(numero1, numero2))
print("Multiplicación:", calcular_multiplicacion(numero1, numero2))
print("División:", calcular_division(numero1, numero2))

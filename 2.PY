#Escribir una función que calcule el área de un círculo dado su radio.

def calcular_area_circulo(radio):
    # fórmula del área del círculo: A = π * r^2
    area = 3.1416 * (radio**2)
    return area

# Ejemplo de uso de la función
radio_ingresado = float(input("Ingresa el radio del círculo: "))
area_del_circulo = calcular_area_circulo(radio_ingresado)
print("El área del círculo con radio {} es: {:.2f}".format(radio_ingresado, area_del_circulo))

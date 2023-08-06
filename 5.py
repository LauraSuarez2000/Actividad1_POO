def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

# Ejemplo de uso de la función
grados_fahrenheit_ingresados = float(input("Ingresa la temperatura en grados Fahrenheit: "))
grados_celsius_calculados = fahrenheit_a_celsius(grados_fahrenheit_ingresados)
print("{} grados Fahrenheit equivalen a {:.2f} grados Celsius.".format(grados_fahrenheit_ingresados, grados_celsius_calculados))

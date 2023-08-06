#Escribir un programa que determine si un número dado es par o impar.

def es_par(numero):

    if numero % 2 == 0:
        return True
    else:
        return False

# Solicitar al usuario ingresar un número
numero_ingresado = int(input("Ingresa un número entero: "))

# Verificar si es par o impar
if es_par(numero_ingresado):
    print("{} es un número par.".format(numero_ingresado))
else:
    print("{} es un número impar.".format(numero_ingresado))

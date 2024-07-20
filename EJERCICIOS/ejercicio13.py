'''
Ejercicio 13: Verificación de Número Primo. Escribe un programa que determine si un número ingresado por el usuario es primo o no.
'''

# Solicitar un número al usuario
numero = int(input("Introduce un número entero: "))

# Función para verificar si el número es primo
def es_primo(n):
    # Casos especiales
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Verificar si el número es primo
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

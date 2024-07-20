'''
Ejercicio 20: Suma de Números en una Lista. Crea un programa que sume todos los números en una lista ingresada por el usuario.
'''

# Solicitar la lista de números
entrada = input("Introduce una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números flotantes
numeros = list(map(float, entrada.split()))

# Calcular la suma de todos los números en la lista
suma = sum(numeros)

# Mostrar el resultado
print(f"La suma de los números en la lista es: {suma:.2f}")

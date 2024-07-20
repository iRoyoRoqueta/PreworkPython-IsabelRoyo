'''
Ejercicio 16: Contador de Números Pares e Impares. Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
'''

# Solicitar la lista de números al usuario
entrada = input("Introduce una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números enteros
numeros = list(map(int, entrada.split()))

# Inicializar los contadores
contador_pares = 0
contador_impares = 0

# Contar números pares e impares
for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

# Mostrar los resultados
print(f"Cantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")

'''
Ejercicio 4: Contador de Vocales. Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
# Solicitar palabra
palabra = input("Introduce una palabra: ")

# Inicializar el contador
contador_vocales = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Contar las vocales en la palabra
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1

# Mostrar el resultado
print(f"El número de vocales en la palabra '{palabra}' es: {contador_vocales}")
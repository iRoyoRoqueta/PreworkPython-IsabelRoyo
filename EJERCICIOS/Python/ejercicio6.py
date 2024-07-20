'''
Ejercicio 6: Verificación de Palíndromo. Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

# Solicitar palabra
palabra = input("Dime una palabra y te confirmaré si es un palíndromo: ")

# Eliminar espacios y convertir a minúsculas para poder compararla
palabra = palabra.replace(" ", "").lower()

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
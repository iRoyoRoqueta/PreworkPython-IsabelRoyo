'''
Ejercicio 5: Suma de Números Pares. Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
suma_pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        suma_pares += numero

# Mostrar resultado
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}")
'''
Ejercicio 9: Conversor de Divisas. Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
'''

# Solicitar dólares
dolares = float(input("Introduce la cantidad en dólares: "))

# Definir la tasa de cambio
tasa_cambio = 0.85

# Calcular euros
euros = dolares * tasa_cambio

# Mostrar el resultado
print(f"{dolares} dólares son {euros:.2f} euros.")
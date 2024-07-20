'''
Ejercicio 17: Conversor de Millas a Kilómetros. Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
'''

# Solicitar la distancia en millas
millas = float(input("Introduce la distancia en millas: "))

# Tasa de conversión millas <> kilómetros
tasa_conversion = 1.60934

# Calcular la distancia en kilómetros
kilometros = millas * tasa_conversion

# Mostrar el resultado
print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")

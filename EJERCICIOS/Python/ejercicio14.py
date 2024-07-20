'''
Ejercicio 14: Calculadora de Descuento. Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
'''

# Solicitar el precio original del artículo al usuario
precio_original = float(input("Introduce el precio original del artículo sin descuento y en euros: "))

# Definir el porcentaje de descuento
descuento = 0.20

# Calcular el monto del descuento
monto_descuento = precio_original * descuento

# Calcular el precio final después del descuento
precio_final = precio_original - monto_descuento

# Mostrar el resultado
print(f"El precio original del artículo es de {precio_original:.2f} euros.")
print(f"El descuento correspondiente es de  {monto_descuento:.2f} euros.")
print(f"El precio final después de aplicar un descuento del 20% es de {precio_final:.2f} euros.")

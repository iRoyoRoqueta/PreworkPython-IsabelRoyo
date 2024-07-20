'''
Ejercicio 2: Calculadora de Propina. Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''
# Función para calcular la propina
def propina_a_pagar(consumicion):
    propina = consumicion * 0.15
    return propina

# Solicitar a la caja registradora que introduzca el coste de la consumición
consumicion = float(input("El precio de lo consumido es de: "))

# Calcular el precio 
monto = consumicion + propina_a_pagar(consumicion)

# Mostrar el resultado
print(f"La cuenta asciende a {monto} euros.")
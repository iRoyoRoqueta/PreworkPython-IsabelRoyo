'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC). Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

# Solicitar el peso y la altura de la persona
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Categorizar el IMC según las categorías estándar de la OMS
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Categoría: {categoria}")
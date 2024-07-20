'''
Ejercicio 12: Calculadora de Área de un Rectángulo Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
'''

# Solicitar la longitud y el ancho del rectángulo
longitud = float(input("Introduce la longitud del rectángulo en centímetros: "))
ancho = float(input("Introduce el ancho del rectángulo en centímetros: "))

# Calcular el área del rectángulo
area = longitud * ancho

# Mostrar el resultado
print(f"El área del rectángulo es: {area:.2f} centímetros cuadrados.")

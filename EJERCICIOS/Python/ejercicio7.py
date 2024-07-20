'''
Ejercicio 7: Calculadora Simple. Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
'''

# Función para realizar la operación que el usuario quiera
def calculadora(num1, num2, operacion):
    if operacion == '1':
        return num1 + num2
    elif operacion == '2':
        return num1 - num2
    elif operacion == '3':
        return num1 * num2
    elif operacion == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

# Solicitar los números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar el menú de operaciones
print("\nSelecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar la operación
operacion = input("Introduce el número de la operación deseada (1/2/3/4): ")

# Realizar la operación y mostrar el resultado
resultado = calculadora(num1, num2, operacion)
print(f"El resultado de la operación es: {resultado}")
'''
Ejercicio 3: Verificación de Edad. Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
'''

# Solicitar edad
edad = int(input("Por favor, introduce tu edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")
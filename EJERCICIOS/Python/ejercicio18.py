'''
Ejercicio 18: Contador de Palabras. Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
'''

# Solicitar una oración al usuario
oracion = input("Escribe una frase: ")

# Dividir la oración en palabras
palabras = oracion.split()

# Contar la cantidad de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"La frase tiene {cantidad_palabras} palabras.")

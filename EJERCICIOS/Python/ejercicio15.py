'''
Ejercicio 15: Conversor de Tiempo. Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

# Solicitar el número de minutos
total_minutos = int(input("Introduce el número de minutos: "))

# Calcular el número de horas y minutos
horas = total_minutos // 60
minutos = total_minutos % 60

# Mostrar el resultado
print(f"{total_minutos} minutos equivalen a {horas} horas y {minutos} minutos.")

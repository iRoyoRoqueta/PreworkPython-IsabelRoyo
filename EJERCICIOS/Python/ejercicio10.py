'''
Ejercicio 10: Determinar el Día de la Semana. Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
# Solicitar el número del día de la semana al usuario

numero_dia = int(input("Introduce un número del 1 al 7 para obtener el día de la semana (1 para lunes, 2 para martes, etc.): "))

# Determinar el día de la semana basado en el número
if numero_dia == 1:
    dia = "Lunes"
elif numero_dia == 2:
    dia = "Martes"
elif numero_dia == 3:
    dia = "Miércoles"
elif numero_dia == 4:
    dia = "Jueves"
elif numero_dia == 5:
    dia = "Viernes"
elif numero_dia == 6:
    dia = "Sábado"
elif numero_dia == 7:
    dia = "Domingo"
else:
    dia = "Número no válido. Debe ser entre 1 y 7."

# Mostrar el resultado
print(f"El día de la semana correspondiente al número {numero_dia} es: {dia}")
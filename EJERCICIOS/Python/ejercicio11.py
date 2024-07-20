'''
Ejercicio 11: Calculadora de Edad Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
'''

from datetime import datetime

# Solicitar el año de nacimiento del usuario
anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

# Obtener el año actual
anio_actual = datetime.now().year

# Calcular la edad
edad = anio_actual - anio_nacimiento

# Mostrar el resultado
print(f"Hace alrededor de {edad} años que naciste. Vamos a calcularlo con exactitud.")

# Opcional: Mensaje adicional si el usuario aún no ha cumplido años este año
mes_actual = datetime.now().month
dia_actual = datetime.now().day

# Solicitar el mes y el día de nacimiento (opcional para precisión)
mes_nacimiento = int(input("Introduce el mes en que naciste (1-12): "))
dia_nacimiento = int(input("Introduce el día en que naciste (1-31): "))

if (mes_nacimiento > mes_actual) or (mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
    edad -= 1

# Mostrar la edad corregida si es necesario
print(f"Tu edad actual es de {edad} años.")

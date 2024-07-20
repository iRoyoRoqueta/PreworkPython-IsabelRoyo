'''
Ejercicio 19: Verificación de Año Bisiesto. Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
'''

# Solicitar el año al usuario
anio = int(input("Introduce un año: "))

# Verificar si el año es bisiesto
def es_bisiesto(anio):
    if (anio % 4 == 0):
        if (anio % 100 == 0):
            if (anio % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Determinar y mostrar si el año es bisiesto
if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")

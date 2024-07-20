'''
1.1 Dado el siguiente diccionario, cambia el valor de la clave "edad" a 25.
    persona = {"nombre": "Juan", "edad": 10}

1.2 Declara una variable "precio" y asígnale el valor 25. Luego, crea una variable "impuesto" y asígnale el valor de "precio" multiplicado por 0.21.
    Muestra ambos valores por consola de esta forma:
    El precio es 25 y el impuesto es 5.25.

1.3 Dado el siguiente diccionario, imprime con un print el valor de la clave "apellido"
    persona = {"nombre": "Juan", "apellido": "Pérez"}
'''
persona = {"nombre": "Juan", "edad": 10}
persona['edad'] = 25

precio = 25
impuesto = precio * 0.21
resultado = 'El precio es ' + str(precio) + ' y el impuesto es ' + str(impuesto)
print(resultado)

persona2 = {"nombre": "Juan", "apellido": "Pérez"}
print(persona2['apellido'])
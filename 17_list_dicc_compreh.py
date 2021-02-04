"""
Sirve para tener una mejor comprehencion del código
Puede a asignarse tanto a listas como a diccionarios

"""

# pares = []

# for num in range(1,31):
#     if num % 2 == 0:
#         pares.append(num)

pares = [num for num in range(1,31) if num % 2 == 0]

cuadrados = {num:num**2 for num in range(1,11)}
#la llave será el num del rango, y el valor es el numero al cuadrado


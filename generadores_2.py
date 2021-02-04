# -*- coding: cp1252 -*-
'''
yield from
-simplifica el código en bucles anidados
-similar a un array 2x2
'''

#el asterisco indica que se recibiran n cant de datos y en forma de tupla
def devuelve_ciudades(*ciudades):
    for cd in ciudades:
        yield from cd

cds_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(cds_devueltas))
print(next(cds_devueltas))

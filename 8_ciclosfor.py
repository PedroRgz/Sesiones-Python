"""
range() arroja una secuencia de numeros empezando de 0
"""

#range(5,40,3) #dara un rango del 5 al 40 de 3 en 3

for i in range(30):
    if i%3==0:
        print(i)
    elif i==22:
        break #termina la iteracion
        #continue --> pasaria directamnt a la siguiente iteracion

#otro ejemplo
"""
s=ferrocarrril
for letra in range(s):
    print(letra) #imprimira todas las letras una por una conforme cada iteracion
"""

'''
Son estructuras que extraen valores de una función
Se almacenan de uno en uno
Cada vez que se genera, se mantiene en un estado pausado
hasta que se solicita el siguiente --> Susp de estado

sustituye el 'return' de una funcion por 'yield' que
construye un objeto iterador
def numspares():
    .
    .
    .
    yield numeros

    #primera llamada [2], suspension
    #segunda llamada [2,4], suspension
    #...

*Son más eficientes
*Utilies con valores infinitos (generar ip's al azar)
'''

def generaPares(lim):
    num =1

    while num < lim:
        yield num*2
        num +=1

cont_pares = generaPares(10)

print(next(cont_pares))
print('relleno')
print(next(cont_pares))
print('relleno')
print(next(cont_pares))
print('relleno')
print(next(cont_pares))
print('relleno')

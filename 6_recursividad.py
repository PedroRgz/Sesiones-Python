#la recursividad es la capacidad de una funcion para llamarse a sí misma dentro de la misma funcion
def factorial(numero):
    """
    La sienguiente funcion se ejecuta solamente cuando el
    numero es 0, de lo contrario, se sigue llamando sobre
    si misma la funcion... cuando llega a 0, que es el caso
    base, evita un inifinte-loop
    """
    if numero == 0:
        #print('en el if = {}'.format(numero))
        return 1

    #print(numero)
    return numero * factorial(numero-1)

if __name__ == '__main__':
    number = int(input('Escribe un numero: '))
    print (factorial(number))

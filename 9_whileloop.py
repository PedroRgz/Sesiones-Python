import random

def run():
    number_found = False
    random_number= random.randint(0,30) #escogerá un número del 0 al 30 al azar

    while not number_found: #not'FALSE => True ; Not 'TRUE' => False
        number = int(input('Intenta con un numero: '))
        if number == random_number:
            print('Felicidades! Lo encontraste!')
            number_found = True
        elif number > random_number:
            print('el número es más pequeño')
        elif number < random_number:
            print('el número es más grande')

if __name__ == '__main__':
    run()

def palind(string):
    rev_letters = []
    for letter in string:
        #para cada letra en la cadena, inserta las letras en el array empezando desde el índice 0
        rev_letters.insert(0, letter)

    rev_word = ''.join(rev_letters) #recibe secuencia de caracteres

    if string == rev_word: return True

    return False

if __name__ == '__main__':
    palabra = str(input('escribe una palabra:'))
    result = palind(palabra)

    if result is True:
        print('{} sí es un palíndromo'.format(palabra))
    else:
        print('{} NO es un palíndromo'.format(palabra))

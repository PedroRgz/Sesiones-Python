import sys

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def read_message(unknown):
    desencriptado = ''

    for i in range(0, len(unknown)):
        if unknown[i]==' ':
            desencriptado += ' '
        else:
            for key,value in KEYS.items():
                if unknown[i] == value:
                    desencriptado += key
    print('La traducción es: {}'.format(desencriptado))

def build_message(text):
    msj_cifrado=''
    for i in range(0, len(text)):
        if text[i] == ' ': 
            msj_cifrado += ' '
        else:
            for key,value in KEYS.items():
                if text[i] == key:
                    msj_cifrado += value
    print('Este es el mensaje: {}'.format(msj_cifrado))

if __name__ == '__main__':
    print('Con este programa puedes: \n[C]ifrar texto\n[D]escifrar texto \n[S]alir')
    instruccion = str(input('Qué quieres realizar?: '))

    while True:
        if instruccion == 'c':
            mensaje = str(input('Escribe el mensaje: '))
            build_message(mensaje)
            #sys.exit()
        elif instruccion == 'd':
            mensaje = str(input('Escribe el mensaje: '))
            read_message(mensaje)
        elif instruccion == 's':
            break
        else:
            print('*Indicacion no encontrada')
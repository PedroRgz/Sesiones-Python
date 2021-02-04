import random

ESTADIOS = [
	'''
	      ------------
	     |            |
	                  |
	                  |
	                  |
	                  ----------
	''',
	'''
	      ------------
	     |            |
	     O            |
	                  |
	                  |
	                  ----------
	''',
	'''
	      ------------
	     |            |
	     O            |
	     ¦            |
	                  |
	                  ----------
	''',
	'''
	      ------------
	     |            |
	     O            |
	    /¦            |
	                  |
	                  ----------
	''',
	'''
	      ------------
	     |            |
	     O            |
	    /¦\           |
	                  |
	                  ----------
	''',
	'''
              ------------
	     |            |
	     O            |
	    /¦\           |
	    /             |
	                  ----------
	''',
	'''
              ------------
	     |            |
	     O            |
	    /¦\           |
	    / \           |
	                  ----------
	'''
]

PALABRAS = [
	'vaca',
	'playa',
	'sonrisa',
	'tumba',
	'salsa',
	'carambola',
	'estufa'
]

def saludo():
	print('B I E N V E N I DO')
	print('        AL        ')
	print('    J U E G O     ')
	print('       D E ')
	print(' A H O R C A D O ')
	
def dibuja_tablero(palabra_oculta, intentos):
	print(ESTADIOS[intentos])
	print('')
	print(palabra_oculta)

def random_word():
	idx = random.randint(0, len(PALABRAS)-1)
	return PALABRAS[idx]

def inicio():
	palabra = random_word()
	palabra_oculta = [' - '] * len(palabra)
	intentos = 0

	dibuja_tablero(palabra_oculta, intentos)

	while intentos<7:
		if palabra_oculta.count(' - ') == 0:
			print('****FELICIDADES! GANASTE!****')
			print('La palabra es: {}'.format(palabra))
			break
		elif intentos == 6:
			print('****ESTAS MUERTO :(****')
			#dibuja_tablero(palabra_oculta, intentos)
			print('F I N . . .')
			break
		else:
			letra = str(input('Escoge una letra: '))
			if is_contain(letra, palabra):
				
				for i in range(0,len(palabra_oculta)):
					if palabra[i]==letra:
						palabra_oculta[i] = letra
				
				dibuja_tablero(palabra_oculta, intentos)
			else:
				intentos +=1
				dibuja_tablero(palabra_oculta, intentos)
				if intentos<6: print('Intenta con otra letra...')


	
def is_contain(word, palabra):
	for letter in palabra:
		if word == letter:
			return True
	
	return False


if __name__=='__main__':
	saludo()
	inicio()
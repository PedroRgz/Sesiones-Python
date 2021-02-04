def just_once(string):
	for i in range(0,len(string)):
		count = 0
		for j in range (0, len(string)):
			if string[i] == string[j] and i != j:
				count += 1
		if count == 0:
			return string[i]
	return '_'

if __name__ == '__main__':
	cadena = str(input('Escribe una secuencia de caracteres: '))

	result = just_once(cadena)

	if result == '_':
		print('Todos los caracteres se repiten más de una vez')
	else:
		print('El caracter no repetido es: {}'.format(result))
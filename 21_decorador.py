'''
Un decoradores una función que recibe otra función 
y regresa una tercera función.

Para reconocer un decorador, puedes ver que tienes 
un arroba sobre la declaración de una función.
'''

def proteccted(func):
	def wrapper(password):
		if password == 'platzi':
			return func()
		else:
			print('la contraseña es incorrecta')

	return wrapper

@proteccted
def protected_func():
	print('Tu contraseña es correcta')

if __name__ == '__main__':
	password = str(input('Ingresa tu contraseña: '))

	protected_func(password)
def foreing_exchange_calculator(ammount):
	mex_to_col_rate = 145.97

	return mex_to_col_rate*ammount


def run():
	print('Calculadora de divisas')
	print('De pesos mexicanos')
	print('')

	ammount = float(input('Ingresa la cantidad de pesos mexicanos: '))

	result = foreing_exchange_calculator(ammount)

	print('${} pesos mexicanos son ${} pesos columbianos'.format(ammount, result))


if __name__ == '__main__':
	run()
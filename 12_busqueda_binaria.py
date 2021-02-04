import random

def make_num_list(size):
	lista_numeros = []
	for i in range(size):
		lista_numeros.append(random.randint(0,size))
	#print(lista_numeros)
	return lista_numeros


def binary_search(find_number, in_this_list, bottom, top):
	mid = int((bottom + top)/2)

	if bottom > top:
		#se llega al indice -1 de la lista, el cual no existe
		print('El número NO está en la lista')
	elif in_this_list[mid] == find_number:
		print('El número sí está en la lista')
	elif in_this_list[mid] > find_number:
		return binary_search(find_number, in_this_list, bottom, mid-1)
	else:
		return binary_search(find_number, in_this_list, mid+1, top)

if __name__ == '__main__':
	size_list = int(input('Dime de qué tamaño la lista: ')) 
	print('Generando lista de numeros...')
	lista_nums = make_num_list(size_list)
	print('La lista comienza a ordenarze...')
	#sorted_list = lista_nums.sort()
	lista_nums.sort()
	#print(lista_nums)
	find_this = int(input('Qué número desea buscar?: '))
	binary_search(find_this, lista_nums, 0, len(lista_nums)-1)
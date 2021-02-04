#la funcion open() abre el archivo
#los archivos pueden ser de texto o binarios
#se tiene que especificar el modo que se maneja el archivo
# r=read
# w=write
# a=append
# r+ = read and write
# SIEMPRE se debe cerrar el archivo con close()
# la mejor forma de manejar archivos es con with

with open('numeros.txt', w) as f:
	for i in range(10):
		f.write(str(i))


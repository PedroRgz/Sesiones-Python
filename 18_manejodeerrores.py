"""
try = el código que puede generar error
except = es el manejo de error
else= se ejecuta si no han ocurrido excepciones
finally = pedazo de código que se ejecuta siempre

Se puede usar la palabra reservada 'raise' + un tipo
de error (que esté dentro de la biblioteca de python)
para lanzar deliveradamente un evento de error
*Se puede crear una clase para nombrar un error
personalizado... (investigar)
"""

#ejemplo de código
def main():
	
	countries = {"mexico": 122, "colombia": 40, "venezuela": 30, "arganetina":49}

	#declaro bandera para detener el ciclo while
	opc = "s"
	while opc == "s":

		#pido el pais a consultar
		country = str(input("Ingresa un pais a consultar ")).lower()

		#intento mostrar la cantidad de habitantes. Si existe muestra la info
		try:
			print("La poblacion de", country, "es: ", countries[country])


		#si la llave no existe muestra que no tiene la info
		except KeyError: #se puede pasar => KeyError as 'nombre' -> ese será el objeto-error
			print("El pais consultado no está en la base de datos intente con otr")

		#pase lo que pase siempre pregunta si quiere seguir consultando
		finally:
			#pido en dato
			opc = str(input("Desea consultar otro pais? s/n \n"))
			#me aseguro de que sea minuscula
			opc=opc.lower()
			#si es distinto de s termino el programa
			if opc != "s":
				print("Adios")

if __name__ == '__main__':
	main()
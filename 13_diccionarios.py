#para iterar sobre los diccionarios-------------
#for llave in diccionario:
#for llave in diccionario.keys():
#for llave in diccionario.values():
#for llave, valor in diccionario.iteritems():
#-----------------------------------------------

califics = {}
califics['anatomia'] = 9
califics['fisiologia']=10
califics['quimica']=8
califics['laboratorio']=9

suma_califics = 0

for valor in califics.values():
	suma_califics += valor

promedio = suma_califics/len(califics.values())

print('Tu promedio es: ')
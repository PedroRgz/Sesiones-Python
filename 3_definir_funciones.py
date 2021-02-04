#la palabra reservada es "def"
import turtle

def main():
    window = turtle.Screen()
    pedro = turtle.Turtle()

    make_square(pedro)

    turtle.mainloop()

def make_square(pedro):
	lenght = int(input('De qué tamaño será el cuadrado?: '))

	for i in range(4):
		make_line_and_turn(pedro, lenght)

def make_line_and_turn(pedro, lenght):
	pedro.forward(lenght)
	pedro.left(90)



#la siguiente funcion define que esta es la funcion principipal, inicial al ejecutarse el archivo
if __name__ == '__main__':
    #4 espacios apra definir el bloque de una funcion
    main()
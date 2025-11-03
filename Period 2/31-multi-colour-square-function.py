import turtle

def draw_multicolour_square(some_turtle, side_length, colours):
    '''Draw a square with some_turtle, where each side is
       side_length long. The colours of the square need to be
       passed in as a list of 4 colours.'''
    for the_colour in colours:
        some_turtle.color(the_colour)
        some_turtle.forward(side_length)
        some_turtle.left(90)
    
window = turtle.Screen()
kavya = turtle.Turtle()
kavya.pensize(5)
kavya.speed(0)

for counter in range(10, 300, 15):
    draw_multicolour_square(kavya, counter, ["red", "green", "blue", "yellow"])
    kavya.forward(10)
    kavya.left(15)
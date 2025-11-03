import turtle

def draw_multicolour_square(some_turtle, side_length, the_colours):
    '''Draws a square with some_turtle, where each side is side_length
       long. The colours of the sides need to be passed in as a list
       of 4 colours.'''
    for some_colour in the_colours:
        some_turtle.color(some_colour)
        some_turtle.forward(side_length)
        some_turtle.left(90)

window = turtle.Screen()
andrew = turtle.Turtle()
andrew.pensize(5)
andrew.speed(0)

for size in range(10, 400, 15):
    draw_multicolour_square(andrew, size, ["red", "green", "blue", "orange"])
    andrew.forward(10)
    andrew.left(15)
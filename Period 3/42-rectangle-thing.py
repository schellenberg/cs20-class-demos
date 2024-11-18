import turtle

def draw_rectangle(a_turtle, short_side_length, long_side_length):
    '''Draws a rectangle with a_turtle, using the long_side_length
       first, then the short_side_length.'''
    for counter in range(2):
        a_turtle.forward(long_side_length)
        a_turtle.left(90)
        a_turtle.forward(short_side_length)
        a_turtle.left(90)

window = turtle.Screen()
zeyad = turtle.Turtle()
zeyad.pensize(5)

for rectangle in range(4):
    draw_rectangle(zeyad, 75, 250)
    zeyad.left(90)
    
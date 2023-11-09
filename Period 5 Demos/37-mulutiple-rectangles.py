import turtle

def draw_rectangle(a_turtle, long_side, short_side):
    '''Draws a rectangle with a_turtle, starting with the long_side, then
       the short_side.'''
    for length in [long_side, short_side, long_side, short_side]:
        a_turtle.forward(length)
        a_turtle.left(90)

canvas = turtle.Screen()
muneeb = turtle.Turtle()
muneeb.pensize(3)

for rectangle in range(4):
    draw_rectangle(muneeb, 200, 50)
    muneeb.left(360/4)

import turtle

def draw_rectangle(some_turtle, short_side_length, long_side_length):
    '''Draws a rectangle using some_turtle, drawing the long_side first
       then the short_side.'''
    for counter in range(2):
        some_turtle.forward(long_side_length)
        some_turtle.left(90)
        some_turtle.forward(short_side_length)
        some_turtle.left(90)

def draw_octagon_rectangle(a_turtle, short_length, long_length):
    '''Draws an octagon shape, made out of 8 rectangles.'''
    for rectangle in range(8):
        draw_rectangle(a_turtle, short_length, long_length)
        a_turtle.left(90)
        a_turtle.forward(short_length)
        a_turtle.right(90)
        a_turtle.left(360/8)

window = turtle.Screen()
emmett = turtle.Turtle()
emmett.pensize(5)
emmett.speed(0)

draw_octagon_rectangle(emmett, 50, 125)

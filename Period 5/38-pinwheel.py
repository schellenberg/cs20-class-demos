import turtle

def draw_rectangle(the_turtle, width, length):
    '''Draws a rectangle with the_turtle. The long side is length, and the
       short side is width.'''
    for l_shape in range(2):
        the_turtle.forward(length)
        the_turtle.left(90)
        the_turtle.forward(width)
        the_turtle.left(90)
    
def draw_pinwheel(a_turtle, long_side, short_side):
    '''Draws four rectangles in a pinwheel shape, using a_turtle.
       The long_side is the long side of each rectangle.
       The short_side is the shorter side of each rectangle.'''
    for rectangle in range(4):
        draw_rectangle(a_turtle, short_side, long_side)
        a_turtle.left(90)
    
canvas = turtle.Screen()
louise = turtle.Turtle()
louise.pensize(5)

draw_pinwheel(louise, 250, 100)


import turtle

def draw_rectangle(the_turtle, width, length):
    '''Draws a rectangle with the_turtle.
       The long side is the length, the short side is the width.'''
    for l_shape in range(2):
        the_turtle.forward(length)
        the_turtle.left(90)
        the_turtle.forward(width)
        the_turtle.left(90)
    
def draw_pinwheel(a_turtle, long_side, short_side):
    '''Draws four rectangles in a pinwheel shape. The long_side is the
       large side of the rectangle, short_side is the short.'''
    for rectangle in range(4):
        draw_rectangle(a_turtle, short_side, long_side)
        a_turtle.left(90)
    
canvas = turtle.Screen()
mary = turtle.Turtle()
mary.pensize(5)

draw_pinwheel(mary, 200, 50)

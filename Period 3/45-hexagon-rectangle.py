import turtle

def draw_rectangle(a_turtle, short_side_length, long_side_length):
    '''Draws a rectangle with a_turtle, using the long_side_length
       first, then the short_side_length.'''
    for counter in range(2):
        a_turtle.forward(long_side_length)
        a_turtle.left(90)
        a_turtle.forward(short_side_length)
        a_turtle.left(90)
    
def draw_hexagon_rectangle(some_turtle, shorter_length, longer_length):
    '''Draws 8 rectangles in a hexagon shape, and uses the shorter_length
       and longer_length for their side lengths.'''
    for rectangle in range(8):
        draw_rectangle(some_turtle, shorter_length, longer_length)
        some_turtle.left(90)
        some_turtle.forward(shorter_length)
        some_turtle.right(90)
        some_turtle.left(360/8)


canvas = turtle.Screen()
hazel = turtle.Turtle()
hazel.pensize(5)
hazel.speed(0)

draw_hexagon_rectangle(hazel, 30, 100)

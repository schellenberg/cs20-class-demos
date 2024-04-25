import turtle

def draw_square(the_turtle, side_length):
    '''Draws a square with the_turtle, where each side is
       side_length long.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

def draw_inner_squares(some_turtle, big_square_size, buffer_size):
    '''Draws two squares, one inside the other. The larger square
       has side lengths of big_square_size, and the distance between
       them is buffer_size.'''
    draw_square(some_turtle, big_square_size)
    some_turtle.penup()
    some_turtle.forward(buffer_size)
    some_turtle.left(90)
    some_turtle.forward(buffer_size)
    some_turtle.right(90)
    some_turtle.pendown()
    draw_square(some_turtle, big_square_size - 2*buffer_size)

window = turtle.Screen()
ella = turtle.Turtle()
ella.pensize(5)

draw_inner_squares(ella, 250, 25)

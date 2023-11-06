import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side length
       is side_length long. Ends at the same spot it started.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(a_turtle, inner_size, gap_size):
    '''Draws a square inside another square, using a_turtle.
       inner_size is the side length of the smaller square.
       gap_size is the distance between the squares.'''
    draw_square(a_turtle, inner_size)
    a_turtle.penup()
    a_turtle.backward(gap_size)
    a_turtle.right(90)
    a_turtle.forward(gap_size)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, inner_size + 2*gap_size)

canvas = turtle.Screen()
michael = turtle.Turtle()
michael.pensize(3)

draw_inner_squares(michael, 150, 20)
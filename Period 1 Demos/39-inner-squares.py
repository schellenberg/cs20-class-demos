import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.
       Ends in the same spot and orientation that it started.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(a_turtle, small_size, gap_size):
    '''Draw a square inside another square.
       Inner square side lengths are small_size long.
       Distance between the squares is gap_size.'''
    draw_square(a_turtle, small_size)
    a_turtle.penup()
    a_turtle.backward(gap_size)
    a_turtle.right(90)
    a_turtle.forward(gap_size)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, small_size + gap_size*2)

window = turtle.Screen()
danny = turtle.Turtle()
danny.pensize(3)

draw_inner_squares(danny, 100, 25)

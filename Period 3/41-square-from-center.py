import turtle

def draw_square(some_turtle, side_length):
    '''Use some_turtle to draw a square, with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_center(a_turtle, side_length):
    '''Draws a square, but starts and ends in the middle of the square.'''
    a_turtle.penup()
    for counter in range(2):
        a_turtle.right(90)
        a_turtle.forward(side_length/2)
    a_turtle.left(180)
    a_turtle.pendown()
    draw_square(a_turtle, side_length)
    a_turtle.penup()
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)

def draw_inner_squares(a_turtle, long_side, short_side):
    '''Draws two squares, with the larger square having side
       lengths of long_side, and the smaller square having
       side lengths of short_side.'''
    draw_square_from_center(a_turtle, long_side)
    draw_square_from_center(a_turtle, short_side)
    
def draw_rotated_sqaures(some_turtle, side_length):
    '''Draw two squares, with one rotated by 45 degrees.'''
    draw_square_from_center(some_turtle, side_length)
    some_turtle.left(45)
    draw_square_from_center(some_turtle, side_length)

def draw_overlapped_squares(some_turtle, side_length):
    '''Draws two squares overlapped.'''
    draw_square(some_turtle, side_length)
    draw_square_from_center(some_turtle, side_length)

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

tarush = turtle.Turtle()
tarush.pensize(5)
# draw_square_from_center(tarush, 200)
# draw_inner_squares(tarush, 200, 150)
# draw_rotated_sqaures(tarush, 200)
draw_overlapped_squares(tarush, 200)
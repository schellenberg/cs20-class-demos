import turtle

def draw_square(some_turtle, side_length):
    '''Use some_turtle to draw a square, with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(a_turtle, long_side, short_side):
    '''Draws two squares, with the larger square having side
       lengths of long_side, and the smaller square having
       side lengths of short_side.'''
    gap = (long_side - short_side) / 2
    draw_square(a_turtle, long_side)
    a_turtle.penup()
    a_turtle.forward(gap)
    a_turtle.left(90)
    a_turtle.forward(gap)
    a_turtle.right(90)
    a_turtle.pendown()
    draw_square(a_turtle, short_side)
    

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

tarush = turtle.Turtle()
tarush.pensize(5)
draw_inner_squares(tarush, 200, 150)
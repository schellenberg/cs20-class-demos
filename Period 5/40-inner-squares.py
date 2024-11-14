import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side
       is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(a_turtle, long_side_length, short_side_length):
    '''Draws two squares, one inside the other. The larger square uses
       long_side_length for each side, and the smaller uses
       short_side_length. The gap between them is calculated by the
       function.'''
    gap = (long_side_length - short_side_length) / 2
    draw_square(a_turtle, long_side_length)
    a_turtle.penup()
    a_turtle.forward(gap)
    a_turtle.left(90)
    a_turtle.forward(gap)
    a_turtle.right(90)
    a_turtle.pendown()
    draw_square(a_turtle, short_side_length)

window = turtle.Screen()
window.bgcolor("lightgreen")

arbe = turtle.Turtle()
arbe.pensize(3)

draw_inner_squares(arbe, 300, 200)


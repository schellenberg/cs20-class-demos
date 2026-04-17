import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square using some_turtle, where each side is
       side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(a_turtle, long_side, short_side):
    '''Draws one smaller square inside a larger square.
       The length of the larger square is long_side.
       The length of the shorter square is short_side.'''
    draw_square(a_turtle, long_side)
    a_turtle.penup()
    a_turtle.forward((long_side - short_side)/2)
    a_turtle.left(90)
    a_turtle.forward((long_side - short_side)/2)
    a_turtle.right(90)
    a_turtle.pendown()
    draw_square(a_turtle, short_side)

window = turtle.Screen()
window.bgcolor("lightgreen")

yakup = turtle.Turtle()
yakup.pensize(5)

#draw inner squares
draw_inner_squares(yakup, 300, 250)


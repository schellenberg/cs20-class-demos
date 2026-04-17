import turtle

def draw_square(my_turtle, side_length):
    '''Draws a square with my_turtle, where each side is side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_inner_squares(a_turtle, long_side, short_side):
    '''Draws a small square inside a large square.
       The large square has side lengths of long_side.
       The small square has side lengths of short_side.'''
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

apipa = turtle.Turtle()
apipa.pensize(5)

draw_inner_squares(apipa, 150, 50)

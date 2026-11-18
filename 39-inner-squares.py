import turtle

def draw_square(a_turtle, side_length):
    '''Draws a square with a_turtle, where each side is side_length long.'''
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)

def draw_inner_squares(some_turtle, short_side, long_side):
    '''Draws two squares using some_turtle. The outer square has
       side lengths of long_side, and the inner square is centered
       inside, and has side lengths of short_side.'''
    draw_square(some_turtle, long_side)
    some_turtle.penup()
    some_turtle.forward((long_side - short_side)/2)
    some_turtle.left(90)
    some_turtle.forward((long_side - short_side)/2)
    some_turtle.right(90)
    some_turtle.pendown()
    draw_square(some_turtle, short_side)

window = turtle.Screen()
window.bgcolor("lightgreen")

himal = turtle.Turtle()
himal.color("blue")
himal.pensize(4)

draw_inner_squares(himal, 175, 250)
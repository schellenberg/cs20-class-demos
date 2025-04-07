import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
def draw_inner_squares(the_turtle, big_side, gap):
    '''Draws a set of two squares with the_turtle.
       The larger side length is big_side.
       The distance between the two squares is gap.'''
    draw_square(the_turtle, big_side)
    the_turtle.penup()
    the_turtle.forward(gap)
    the_turtle.left(90)
    the_turtle.forward(gap)
    the_turtle.right(90)
    the_turtle.pendown()
    draw_square(the_turtle, big_side - gap * 2)
        
canvas = turtle.Screen()
john = turtle.Turtle()

draw_inner_squares(john, 200, 50)

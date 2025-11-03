import turtle

def draw_square(the_turtle, side_length):
    '''Draws a square with the_turtle, where each
       side is side_length long.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

canvas = turtle.Screen()
noah = turtle.Turtle()
bertin = turtle.Turtle()
bertin.color("red")

draw_square(noah, 100)
draw_square(bertin, 300)

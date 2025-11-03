import turtle

def draw_square(the_turtle, side_length):
    '''Draw a square with the_turtle, where each side
       is side_length long'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)


canvas = turtle.Screen()
matthew = turtle.Turtle()
nathan = turtle.Turtle()
nathan.color("red")

draw_square(matthew, 150)
draw_square(nathan, 300)

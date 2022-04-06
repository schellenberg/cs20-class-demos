import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow c shape. Assumes the width_of_c is smaller than the
       the longest_side_length.'''
    
    long = longest_side_length
    med = long - width_of_c
    small = long - 2*width_of_c
    width = width_of_c
    
    #slightly adapted from Andrew
    for distance in [small, width, med, long, med, width, small, 0, 0, small]:
        a_turtle.forward(distance)
        a_turtle.right(90)

canvas = turtle.Screen()

aj = turtle.Turtle()
aj.pensize(5)

draw_c(aj, 300, 75)
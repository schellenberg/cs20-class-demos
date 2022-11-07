import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''a_turtle -> turtle.Turtle() object
       longest_side_length -> integer
       width_of_c -> integer
       
       Draws a hollow C shape. Assumes longest side is more
       than twice the length of the width.'''
    a = longest_side_length
    b = longest_side_length - width_of_c
    c = width_of_c
    d = longest_side_length - 2*width_of_c
    
    for side in [b, c, a, a, a, c, b, -d]:
        a_turtle.forward(side)
        a_turtle.left(90)

canvas = turtle.Screen()
daniyal = turtle.Turtle()
daniyal.pensize(5)

draw_c(daniyal, 250, 100)
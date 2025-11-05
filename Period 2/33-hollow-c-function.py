import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow C shape with a_turtle. The side lengths are
       calculated by using the longest_side_length and the
       width_of_c.'''
    l = longest_side_length
    m = longest_side_length - width_of_c
    s = width_of_c
    for step in [m, s, l, l, l, s, m, -(l-2*s)]:
        a_turtle.forward(step)
        a_turtle.left(90)

canvas = turtle.Screen()
nathan = turtle.Turtle()
nathan.pensize(3)

draw_c(nathan, 300, 100)
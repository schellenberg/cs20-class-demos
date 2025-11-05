import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow C shape with a_turtle. The side lengths
       are calculated from the longest_side_length and the
       width_of_c.'''
    l = longest_side_length
    m = longest_side_length - width_of_c
    s = width_of_c
    end = -(longest_side_length - 2*width_of_c)
    for step in [m, s, l, l, l, s, m, end]:
        yasin.forward(step)
        yasin.left(90)

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

yasin = turtle.Turtle()
yasin.shape("turtle")

draw_c(yasin, 400, 150)
    
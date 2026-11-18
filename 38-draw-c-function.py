import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow C shape with a_turtle. The longest side is
       longest_side_length long, and the other sides are calculated
       using width_of_c.'''
    l = longest_side_length
    w = width_of_c
    for side in [l-w, w, l, l, l, w, l-w, -(l-2*w)]:
        a_turtle.forward(side)
        a_turtle.right(90)
    

canvas = turtle.Screen()

nikita = turtle.Turtle()
nikita.shape("turtle")
nikita.pensize(4)

draw_c(nikita, 400, 80)

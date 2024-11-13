import turtle

def draw_cross(some_turtle, side_length):
    '''Draws a cross shape with some_turtle, where each side
       is side_length long.'''
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow c, calculating the side lengths from
       longest_side_length and width_of_c.'''
    l = longest_side_length
    w = width_of_c
    for i in [l-w, w, l, l, l, w, l-w, -(l - 2*w)]:
        a_turtle.forward(i)
        a_turtle.right(90)


window = turtle.Screen()
dracen = turtle.Turtle()
dracen.pensize(5)

#draw_cross(dracen, 50)
draw_c(dracen, 200, 50)

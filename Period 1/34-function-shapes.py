import turtle

def draw_cross(some_turtle, side_length):
    '''Draws a cross shape using some_turtle, where each side is side_length long.'''
    for u_shape in range(4):
        for angle in [-90, -90, 90]:
            some_turtle.forward(side_length)
            some_turtle.left(angle)
    
def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow C shape with a_turtle. The longest_side_length
       determines how big it is, and the width_of_c lets us calculate
       the smaller sides.'''
    s = width_of_c
    m = longest_side_length - width_of_c
    l = longest_side_length
    end = longest_side_length - 2 * width_of_c
    for length in [m, s, l, l, l, s, m, -end]:
        a_turtle.forward(length)
        a_turtle.left(90)

canvas = turtle.Screen()
liam = turtle.Turtle()

# draw_cross(liam, 50)
draw_c(liam, 200, 75)
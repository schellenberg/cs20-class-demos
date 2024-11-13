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
    '''Draws a hollow c shape, and calculates how large each
       side should be based on longest_side_length and the
       width_of_c.'''
    w = width_of_c
    l = longest_side_length
    for length in [l-w, w, l, l, l, w, l-w, 0, 0, l-2*w]:
        a_turtle.forward(length)
        a_turtle.right(90)


window = turtle.Screen()
ben = turtle.Turtle()
ben.pensize(3)

#draw_cross(ben, 50)
draw_c(ben, 300, 25)
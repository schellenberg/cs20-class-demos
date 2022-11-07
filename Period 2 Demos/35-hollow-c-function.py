import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''a_turtle -> turtle.Turtle() object
       longest_side_length -> integer
       width_of_c -> integer
    
       Draws a hollow c shape, with the given sizes.'''
    a = longest_side_length
    b = longest_side_length - width_of_c
    c = longest_side_length - width_of_c*2
    d = width_of_c
    steps = [b, d, a, a, a, d, b, 0, 0, c]
    for side in steps:
        a_turtle.forward(side)
        a_turtle.left(90)


canvas = turtle.Screen()
zoe_ann = turtle.Turtle()
zoe_ann.pensize(4)

draw_c(zoe_ann, 300, 75)
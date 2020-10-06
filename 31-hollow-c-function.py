import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow c shape with a_turtle'''
    inner_horizontal = longest_side_length - width_of_c
    inner_vertical = longest_side_length - 2 * width_of_c
    
    lengths = [inner_horizontal, width_of_c, longest_side_length,
               longest_side_length, longest_side_length, width_of_c,
               inner_horizontal]
    
    for side in lengths:
        a_turtle.forward(side)
        a_turtle.right(90)
        
    a_turtle.right(180)
    a_turtle.forward(inner_vertical)

canvas = turtle.Screen()
jack = turtle.Turtle()
jack.pensize(5)

draw_c(jack, 300, 130)
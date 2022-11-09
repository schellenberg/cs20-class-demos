import turtle

def draw_triangle(my_turtle, side_length):
    '''my_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a triangle with the given turtle, with each side
       being side_length long.'''
    for side in range(3):
        my_turtle.forward(side_length)
        my_turtle.left(360/3)

def draw_pinwheel(some_turtle, length_of_side):
    '''some_turtle -> turtle.Turtle() object
       length_of_side -> integer
       
       Draws a shape made of 6 triangles, with each side of the
       the triangle being length_of_side long.'''
    for triangle in range(6):
        draw_triangle(some_turtle, length_of_side)
        some_turtle.left(360/6)

window = turtle.Screen()
tobias = turtle.Turtle()
tobias.pensize(4)

draw_pinwheel(tobias, 150)
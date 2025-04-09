import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a triangle using a_turtle, with each side being side_length long.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

def draw_triangle_pentagon(the_turtle, length_of_side):
    '''Draws 6 triangles in a pentagon shape.'''
    for triangle in range(6):
        draw_triangle(the_turtle, length_of_side)
        the_turtle.left(60)

canvas = turtle.Screen()
aidan = turtle.Turtle()
aidan.pensize(5)

draw_triangle_pentagon(aidan, 150)


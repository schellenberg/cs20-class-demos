import turtle

def draw_triangle(some_turtle, side_length):
    '''Draws an equilateral triangle.'''
    for side in range(3):
        some_turtle.forward(side_length)
        some_turtle.left(360/3)

def draw_triangle_stop_sign(a_turtle, side_length):
    '''Draws a bunch of triangles, which kinda look like a stop sign.'''
    for triangle in range(6):
        draw_triangle(a_turtle, side_length)
        a_turtle.left(360/6)

canvas = turtle.Screen()
mo = turtle.Turtle()
mo.pensize(5)

draw_triangle_stop_sign(mo, 150)
    

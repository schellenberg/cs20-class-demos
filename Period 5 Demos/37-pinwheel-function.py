import turtle

def draw_triangle(some_turtle, side_length):
    '''some_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a triangle with some_turtle, where each side is
       side_length long.'''
    for side in range(3):
        some_turtle.forward(side_length)
        some_turtle.left(360/3)

def draw_pinwheel(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a shape made up of 6 triangles, where each triangle
       has sides that are side_length long.'''
    for triangle in range(6):
        draw_triangle(a_turtle, side_length)
        a_turtle.left(60)

screen = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(5)

draw_pinwheel(alex, 50)
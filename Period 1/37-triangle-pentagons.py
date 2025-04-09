import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a triangle with a_turtle, each side being side_length long.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

def draw_pentagon_triangles(some_turtle, side_length):
    '''Draws a pentagon made out of 6 triangles. Uses some_turtle, and each side length is side_length long.'''
    for triangle in range(6):
        draw_triangle(some_turtle, side_length)
        some_turtle.left(60)


canvas = turtle.Screen()
zara = turtle.Turtle()
zara.pensize(5)

draw_pentagon_triangles(zara, 100)

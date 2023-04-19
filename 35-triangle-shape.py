import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a equilateral triangle with side_length sides.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

canvas = turtle.Screen()
ben = turtle.Turtle()
ben.pensize(5)

for triangle in range(6):
    draw_triangle(ben, 200)
    ben.left(360/6)

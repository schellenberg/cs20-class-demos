import turtle

def draw_triangle(some_turtle, side_length):
    '''Draws a triangle with some_turtle, where each side is side_length long.'''
    for side in range(3):
        some_turtle.forward(side_length)
        some_turtle.left(360/3)

canvas = turtle.Screen()
abedin = turtle.Turtle()
abedin.pensize(3)

for triangle in range(6):
    draw_triangle(abedin, 150)
    abedin.left(360/6)

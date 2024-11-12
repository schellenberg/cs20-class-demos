import turtle

def draw_square(some_turtle, side_length):
    '''Use some_turtle to draw a square, with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

tarush = turtle.Turtle()
tarush.pensize(5)
draw_square(tarush, 200)

draw_square(tarush, 100)
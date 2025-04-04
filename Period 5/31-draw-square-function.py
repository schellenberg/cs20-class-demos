import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

canvas = turtle.Screen()
canvas.bgcolor("lightblue")

irfan = turtle.Turtle()
irfan.color("red")
irfan.shape("turtle")

ethan = turtle.Turtle()
ethan.color("blue")

draw_square(irfan, 150)
draw_square(ethan, 300)

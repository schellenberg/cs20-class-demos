import turtle

def draw_rectangle(some_turtle, short_side, long_side):
    for sides in range(2):
        some_turtle.forward(short_side)
        some_turtle.left(90)
        some_turtle.forward(long_side)
        some_turtle.left(90)

def draw_octopus(a_turtle, short_length, long_length):
    for rectangle in range(8):
        draw_rectangle(a_turtle, short_length, long_length)
        a_turtle.forward(short_length)
        a_turtle.right(360/8)

canvas = turtle.Screen()
remi = turtle.Turtle()
remi.pensize(4)

draw_octopus(remi, 25, 150)

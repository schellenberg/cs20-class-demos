import turtle

def draw_rectangle(some_turtle, width, height):
    for l_shape in range(2):
        some_turtle.forward(width)
        some_turtle.left(90)
        some_turtle.forward(height)
        some_turtle.left(90)

canvas = turtle.Screen()

anu = turtle.Turtle()
anu.pensize(4)

for rectangle in range(4):
    draw_rectangle(anu, 200, 75)
    anu.left(90)

import turtle

window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

def draw_triangle(some_turtle, side_length):
    for counter in range(3):
        some_turtle.forward(side_length)
        some_turtle.left(360/3)

for counter in range(6):
    draw_triangle(pen, 100)
    pen.left(360/6)
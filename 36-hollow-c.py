import turtle

canvas = turtle.Screen()
noah = turtle.Turtle()
noah.pensize(4)

for side in [250, 50, 300, 300, 300, 50, 250]:
    noah.forward(side)
    noah.left(90)

noah.left(180)
noah.forward(200)

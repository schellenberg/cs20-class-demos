import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

enzo = turtle.Turtle()
enzo.shape("turtle")
enzo.color("blue")
enzo.penup()
enzo.speed(0)

for step in range(10, 150, 2):
    enzo.stamp()
    enzo.forward(step)
    enzo.right(25)
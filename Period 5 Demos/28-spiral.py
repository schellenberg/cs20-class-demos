import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

nathan = turtle.Turtle()
nathan.shape("turtle")
nathan.color("blue")
nathan.penup()
nathan.speed(0)

for step in range(20, 150, 2):
    nathan.stamp()
    nathan.forward(step)
    nathan.left(37)

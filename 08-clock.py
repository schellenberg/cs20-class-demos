import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.pensize(3)

for tick_mark in range(12):
    alex.penup()
    alex.forward(150)
    alex.pendown()
    alex.forward(30)
    alex.penup()
    alex.forward(30)
    alex.stamp()
    alex.backward(210)
    alex.left(360/12)

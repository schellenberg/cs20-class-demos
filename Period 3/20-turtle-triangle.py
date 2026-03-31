# Triangle Turtle Demo

import turtle

#setting up the window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setting up the turtle
jasper = turtle.Turtle()
jasper.shape("turtle")
jasper.color("darkgreen")
jasper.pensize(5)

#drawing the triangle
for counter in range(3):
    jasper.forward(200)
    jasper.left(120)
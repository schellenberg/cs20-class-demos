# Turtle Graphics Intro

import turtle

#setting up the window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setting up the turtle
eric = turtle.Turtle()
eric.shape("turtle")
eric.color("blue")
eric.pensize(5)

#drawing a triangle
for side in range(3):
    eric.left(120)
    eric.forward(150)
    
#exit when user clicks
canvas.exitonclick()
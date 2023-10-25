#draw a triangle

import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

cherry = turtle.Turtle()
cherry.color("blue")
cherry.pensize(4)
cherry.shape("turtle")

for side in range(3):
    cherry.forward(200)
    cherry.left(360/3)
    
cherry.penup()
cherry.back(75)

canvas.exitonclick()
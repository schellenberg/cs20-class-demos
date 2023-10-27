# draw a clock

import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

william = turtle.Turtle()
william.color("blue")
william.shape("turtle")
william.pensize(4)

for hour in range(12):
    #hour tick mark
    william.penup()
    william.forward(100)
    william.pendown()
    william.forward(20)
    william.penup()
    william.forward(20)
    william.stamp()
    william.backward(140)
    william.left(360/12)


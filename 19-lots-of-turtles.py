# lots of turtles demo

import turtle

canvas = turtle.Screen()

aman = turtle.Turtle()
aman.color("blue")
aman.pensize(5)
aman.shape("turtle")

peter = turtle.Turtle()
peter.color("green")
peter.shape("square")

for some_color in ["red","blue","yellow","purple"]:
    aman.color(some_color)
    aman.forward(100)
    aman.left(90)

peter.left(90)
peter.forward(50)
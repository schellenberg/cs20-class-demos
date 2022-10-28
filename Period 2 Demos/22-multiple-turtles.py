#pentagon drawing

import turtle

#setup window
window = turtle.Screen()
window.bgcolor("black")

#setup turtles
harpreet = turtle.Turtle()
harpreet.shape("turtle")
harpreet.color("white")
harpreet.pensize(10)

brayden = turtle.Turtle()
brayden.shape("turtle")
brayden.color("green")
brayden.pensize(5)

#draw pentagon
for side in range(5):
    harpreet.forward(150)
    harpreet.left(360/5)


#draws a triangle
for side in range(3):
    brayden.forward(200)
    brayden.left(360/3)

# turtle clock

import turtle

#create screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#create turtle
ivy = turtle.Turtle()
ivy.shape("turtle")
ivy.color("blue")
ivy.pensize(4)

#draw clock
for tick in range(12):
    #draw one tick mark
    ivy.penup()
    ivy.forward(125)
    ivy.pendown()
    ivy.forward(25)
    ivy.penup()
    ivy.forward(25)
    ivy.stamp()
    ivy.backward(175)
    
    #turn to get ready for next tick mark
    ivy.left(360/12)

# Drawing a Clock

import turtle

# create window, and set it's color
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

# create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color("blue")
bree.shape("turtle")
bree.pensize(3)

for tick_mark in range(12):
    # draw one tick mark
    bree.up()
    bree.forward(120)
    bree.down()
    bree.forward(10)
    bree.up()
    bree.forward(20)
    bree.stamp()
    bree.backward(150)

    #rotate to get ready to draw the next tick mark
    bree.left(360/12)
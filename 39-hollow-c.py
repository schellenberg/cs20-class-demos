# Hollow C Practice Problem

import turtle

window = turtle.Screen()

jared = turtle.Turtle()
jared.pensize(3)

for side in [80, 20, 100, 100, 100, 20, 80]:
    jared.forward(side)
    jared.left(90)

jared.left(180)
jared.forward(60)
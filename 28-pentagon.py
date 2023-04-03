#draw a pentagon (5 sided polygon)

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

jace = turtle.Turtle()
jace.shape("turtle")
jace.color("red")
jace.pensize(5)
jace.penup()

for side in range(5):
    jace.forward(100)
    jace.left(360/5)
    jace.stamp()
    
    
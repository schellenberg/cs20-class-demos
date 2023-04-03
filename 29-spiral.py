#draw a spiral

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

jace = turtle.Turtle()
jace.shape("turtle")
jace.color("red")
jace.pensize(5)
jace.penup()
jace.speed(0)

for side in range(5, 500):
    jace.stamp()
    jace.forward(side)
    jace.left(50)
    
    
    

import turtle

#setup window and turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
nathan = turtle.Turtle()
nathan.color("purple")
nathan.pensize(8)

#draw triangle
for turns in range(3):
    nathan.forward(150)
    nathan.left(120)

window.exitonclick()
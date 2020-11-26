# Multiple Turtles Demo

import turtle

# set up the window
window = turtle.Screen()
window.bgcolor("blue")

# set up first turtle
robin = turtle.Turtle()
robin.color("red")
robin.shape("turtle")

# set up second turtle
lucy = turtle.Turtle()
lucy.color("yellow")
lucy.shape("turtle")
lucy.pensize(5)

robin.forward(50)
for some_color in ["green","red","white","purple"]:
    lucy.color(some_color)
    lucy.left(90)
    lucy.forward(100)

window.exitonclick()
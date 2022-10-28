import turtle

canvas = turtle.Screen()
heath = turtle.Turtle()
heath.pensize(10)

for the_color in ["green", "blue", "yellow", "red"]:
    heath.color(the_color)
    heath.forward(200)
    heath.left(90)
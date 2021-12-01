import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

uday = turtle.Turtle()
uday.color("purple")
uday.pensize(5)

for side in range(4):
    uday.forward(100)
    uday.left(90)

#canvas.exitonclick()
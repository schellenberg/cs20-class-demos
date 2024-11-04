import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

emmett = turtle.Turtle()
emmett.shape("turtle")
emmett.color("red")
emmett.penup()
emmett.speed(0)

for counter in range(10, 200, 3):
    emmett.stamp()
    emmett.forward(counter)
    emmett.right(50)

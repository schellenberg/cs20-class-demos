import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

cooper = turtle.Turtle()
cooper.shape("turtle")
cooper.pensize(3)
cooper.penup()
cooper.speed(0)

for size in range(10, 150, 2):
    cooper.stamp()
    cooper.forward(size)
    cooper.right(25)

canvas.exitonclick()

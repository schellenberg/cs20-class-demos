import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

wyatt = turtle.Turtle()
wyatt.color("blue")
wyatt.shape("turtle")
wyatt.penup()
wyatt.speed(0)

for step in range(5, 200):
    wyatt.stamp()
    wyatt.forward(step)
    wyatt.left(20)

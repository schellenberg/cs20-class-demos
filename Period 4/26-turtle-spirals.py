import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

yixi = turtle.Turtle()
yixi.shape("turtle")
yixi.speed(0)
yixi.penup()

for step in range(10, 200, 2):
    yixi.forward(step)
    yixi.left(50)
    yixi.stamp()
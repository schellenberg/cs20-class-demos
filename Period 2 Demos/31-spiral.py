import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

safin = turtle.Turtle()
safin.color("red")
safin.shape("turtle")
safin.penup()
safin.speed(0)

for movement in range(5, 150, 2):
    safin.stamp()
    safin.forward(movement)
    safin.right(25)
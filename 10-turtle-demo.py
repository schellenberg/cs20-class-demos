import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

shane = turtle.Turtle()
shane.pensize(5)
shane.shape("turtle")
shane.color("green")

for side in range(4):
    shane.forward(100)
    shane.left(90)

#canvas.exitonclick()
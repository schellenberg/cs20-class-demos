import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

cash = turtle.Turtle()
cash.shape("turtle")
cash.color("red")
cash.pensize(5)

#draw a triangle
for side in range(3):
    cash.forward(200)
    cash.left(360/3)

canvas.exitonclick()
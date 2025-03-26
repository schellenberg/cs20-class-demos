import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

zara = turtle.Turtle()
zara.color("lightblue")
zara.pensize(5)

#draw a triangle
for side in range(3):
    zara.forward(100)
    zara.left(360/3)

canvas.exitonclick()
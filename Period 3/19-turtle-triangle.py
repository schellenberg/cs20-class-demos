import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

amy = turtle.Turtle()
amy.shape("turtle")
amy.color("pink")
amy.pensize(10)

#draw a triangle
for some_side in range(3):
    amy.forward(100)
    amy.left(360/3)

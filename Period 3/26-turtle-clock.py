import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

charlie = turtle.Turtle()
charlie.shape("turtle")
charlie.color("blue")
charlie.pensize(4)

for hand in range(12):
    #one tick mark
    charlie.penup()
    charlie.forward(100)
    charlie.pendown()
    charlie.forward(25)
    charlie.penup()
    charlie.forward(25)
    charlie.stamp()
    charlie.backward(150)

    charlie.left(360/12)
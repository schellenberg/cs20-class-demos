import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

mason = turtle.Turtle()
mason.color("blue")
mason.shape("turtle")
mason.pensize(4)

for hour in range(12):
    #one hour tick mark
    mason.penup()
    mason.forward(150)
    mason.pendown()
    mason.forward(20)
    mason.penup()
    mason.forward(20)
    mason.stamp()
    mason.backward(190)

    mason.left(360/12)

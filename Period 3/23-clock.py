import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

navya = turtle.Turtle()
navya.shape("turtle")
navya.color("blue")
navya.pensize(5)

for hour in range(12):
    #draw one tick mark
    navya.penup()
    navya.forward(125)
    navya.pendown()
    navya.forward(20)
    navya.penup()
    navya.forward(20)
    navya.stamp()
    navya.backward(165)

    navya.left(360/12)

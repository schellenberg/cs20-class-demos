import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

musa = turtle.Turtle()
musa.shape("turtle")
musa.color("blue")
musa.pensize(5)

for hand in range(12):
    #one tick mark
    musa.penup()
    musa.forward(100)
    musa.pendown()
    musa.forward(25)
    musa.penup()
    musa.forward(25)
    musa.stamp()
    musa.backward(150)

    musa.left(360/12)

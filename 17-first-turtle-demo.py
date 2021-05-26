import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

hayden = turtle.Turtle()
hayden.shape("turtle")
hayden.color("blue")
hayden.pensize(4)

for side in range(4):
    hayden.forward(150)
    hayden.left(90)


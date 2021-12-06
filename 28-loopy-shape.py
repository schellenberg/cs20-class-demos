import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

mia = turtle.Turtle()
mia.color("red")
mia.shape("turtle")
mia.pensize(5)
mia.penup()

for tick in range(12):
    mia.forward(150)
    mia.pendown()
    mia.forward(25)
    mia.penup()
    mia.forward(25)
    mia.stamp()
    mia.backward(200)
    mia.left(360/12)


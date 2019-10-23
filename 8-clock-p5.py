import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

jacob = turtle.Turtle()
jacob.color("blue")
jacob.pensize(5)
jacob.shape("turtle")

for ticks in range(12):
    jacob.penup()
    jacob.forward(150)
    jacob.pendown()
    jacob.forward(30)
    jacob.penup()
    jacob.forward(30)
    jacob.stamp()
    jacob.backward(210)
    jacob.left(360/12)

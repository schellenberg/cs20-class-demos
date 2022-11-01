import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

joel = turtle.Turtle()
joel.shape("turtle")
joel.color("blue")
joel.pensize(5)

for hour in range(12):
    joel.penup()
    joel.forward(200)
    joel.pendown()
    joel.forward(25)
    joel.penup()
    joel.forward(25)
    joel.stamp()
    joel.backward(250)
    joel.left(360/12)

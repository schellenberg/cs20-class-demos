import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

haidyn = turtle.Turtle()
haidyn.color("blue")
haidyn.shape("turtle")
haidyn.pensize(4)
             

for hour in range(12):
    #one tick mark
    haidyn.penup()
    haidyn.forward(150)
    haidyn.pendown()
    haidyn.forward(25)
    haidyn.penup()
    haidyn.forward(25)
    haidyn.stamp()

    haidyn.backward(200)
    haidyn.left(360/12)

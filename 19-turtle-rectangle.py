import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

soren = turtle.Turtle()
soren.color("purple")
soren.shape("turtle")
soren.pensize(5)

#make soren draw a rectangle
for counter in range(2):
    soren.forward(100)
    soren.left(90)
    soren.forward(200)
    soren.left(90)

window.exitonclick()
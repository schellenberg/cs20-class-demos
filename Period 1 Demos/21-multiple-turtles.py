import turtle

screen = turtle.Screen()
screen.bgcolor("gray")

mark = turtle.Turtle()
mark.shape("turtle")
mark.pensize(5)
mark.color("yellow")

radia = turtle.Turtle()
radia.color("blue")
radia.pensize(3)

# mark draws me a pentagon (5 sided shape)
for side in range(5):
    mark.forward(150)
    mark.left(360/5)

# radia draws me a square
radia.penup()
radia.backward(275)
radia.pendown()
radia.speed(1)
for r in range(4):
    radia.forward(150)
    radia.left(90)
    


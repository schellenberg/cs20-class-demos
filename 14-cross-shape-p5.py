import turtle

canvas = turtle.Screen()
iftemum = turtle.Turtle()
iftemum.shape("turtle")
iftemum.pensize(5)

for leg in range(4):
    for side in range(3):
        iftemum.forward(100)
        iftemum.left(90)
    iftemum.left(180)

import turtle

window = turtle.Screen()
ben = turtle.Turtle()
ben.pensize(3)

for u_shape in range(4):
    for side in range(3):
        ben.forward(100)
        ben.left(90)
    ben.left(180)

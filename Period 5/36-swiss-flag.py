import turtle

window = turtle.Screen()
dracen = turtle.Turtle()
dracen.pensize(5)

for u_shape in range(4):
    for side in range(3):
        dracen.forward(150)
        dracen.left(90)
    dracen.left(180)

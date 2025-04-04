import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightblue")

trey = turtle.Turtle()
trey.color("red")
trey.pensize(5)

# draw cross shape
for u_shape in range(4):
    for angle in [-90, -90, 90]:
        trey.forward(100)
        trey.left(angle)

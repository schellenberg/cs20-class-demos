import turtle

canvas = turtle.Screen()
eric = turtle.Turtle()
eric.pensize(4)

for side in [200, 50, 250, 250, 250, 50, 200, -150]:
    eric.forward(side)
    eric.left(90)


# eric.forward(200)
# eric.left(90)
# eric.forward(50)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(50)
# eric.left(90)
# eric.forward(200)
# eric.right(90)
# eric.forward(150)
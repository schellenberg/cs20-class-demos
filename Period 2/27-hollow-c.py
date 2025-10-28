import turtle

canvas = turtle.Screen()
nathan = turtle.Turtle()
nathan.pensize(3)

#first version
# nathan.forward(200)
# nathan.left(90)
# nathan.forward(50)
# nathan.left(90)
# nathan.forward(150)
# nathan.right(90)
# nathan.forward(100)
# nathan.right(90)
# nathan.forward(150)
# nathan.left(90)
# nathan.forward(50)
# nathan.left(90)
# nathan.forward(200)
# nathan.left(90)
# nathan.forward(200)


#second version
# nathan.right(90)
# for length in [200, 25, 225, 250, 225, 25, 200]:
#     nathan.left(90)
#     nathan.forward(length)
# nathan.right(90)
# nathan.forward(200)


#third version
# for step in [150, 50, 200, 200, 200, 50, 150]:
#     nathan.forward(step)
#     nathan.left(90)
# nathan.backward(100)


#fourth version
for step in [150, 50, 200, 200, 200, 50, 150, -100]:
    nathan.forward(step)
    nathan.left(90)


import turtle

canvas = turtle.Screen()
leo = turtle.Turtle()
leo.pensize(5)

#schellenberg's method
for side in [175, 25, 200, 200, 200, 25, 175, -150]:
    leo.forward(side)
    leo.left(90)


# #ghassane's method
# leo.backward(200)
# leo.left(90)
# leo.forward(200)
# leo.right(90)
# leo.forward(200)
# leo.right(90)
# leo.forward(30)
# leo.right(90)
# leo.forward(165)
# leo.left(90)
# leo.forward(140)
# leo.left(90)
# leo.forward(165)
# leo.right(90)
# leo.forward(30)






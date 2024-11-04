import turtle

window = turtle.Screen()
annie = turtle.Turtle()
annie.pensize(5)

#alasdair's adapted solution
for length in [200, 50, 250, 250, 250, 50, 200, 0, 0, 150]:
    annie.forward(length)
    annie.right(90)

#alasdair's solution
# for length in [200, 50, 250, 250, 250, 50, 200]:
#     annie.forward(length)
#     annie.right(90)
# annie.left(180)
# annie.forward(150)

#wynn's solution
# annie.left(90)
# annie.forward(35)
# annie.left(90)
# for line in range(3):
#     annie.forward(200)
#     annie.right(90)
# annie.left(180)
# annie.forward(35)
# annie.left(90)
# annie.forward(235)
# annie.left(90)
# annie.forward(270)
# annie.left(90)
# annie.forward(235)

#annie's solution
# annie.forward(200)
# annie.left(90)
# annie.forward(40)
# annie.left(90)
# annie.forward(150)
# annie.right(90)
# annie.forward(120)
# annie.right(90)
# annie.forward(150)
# annie.left(90)
# annie.forward(40)
# annie.left(90)
# annie.forward(200)
# annie.left(90)
# annie.forward(200)

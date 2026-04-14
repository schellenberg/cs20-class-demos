import turtle

canvas = turtle.Screen()
ifsan = turtle.Turtle()
ifsan.pensize(5)

#asher's version but better
for distance in [175, 25, 200, 200, 200, 25, 175, -150]:
    ifsan.forward(distance)
    ifsan.left(90)

#asher's version
# for distance in [175, 25, 200, 200, 200, 25, 175]:
#     ifsan.forward(distance)
#     ifsan.left(90)
# ifsan.right(180)
# ifsan.forward(150)

#jasper's version -- interesting, and uses tuples
# for place in [(200, 0), (200, 25), (25, 25), (25, 175), (200, 175), (200, 200), (0, 200), (0, 0)]:
#     ifsan.goto(place)

#common solution
# ifsan.forward(200)
# ifsan.left(90)
# ifsan.forward(25)
# ifsan.left(90)
# ifsan.forward(175)
# ifsan.right(90)
# ifsan.forward(150)
# ifsan.right(90)
# ifsan.forward(175)
# ifsan.left(90)
# ifsan.forward(25)
# ifsan.left(90)
# ifsan.forward(200)
# ifsan.left(90)
# ifsan.forward(200)
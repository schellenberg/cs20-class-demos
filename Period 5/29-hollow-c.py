import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

grayer = turtle.Turtle()
grayer.pensize(10)

#method 1
# grayer.forward(160)
# grayer.left(90)
# grayer.forward(40)
# grayer.left(90)
# grayer.forward(200)
# grayer.left(90)
# grayer.forward(200)
# grayer.left(90)
# grayer.forward(200)
# grayer.left(90)
# grayer.forward(40)
# grayer.left(90)
# grayer.forward(160)
# grayer.right(90)
# grayer.forward(120)

#method 2
# side = 0
# for distance in [180, 20, 200, 200, 200, 20, 180, 160]:
#     grayer.forward(distance)
#     if side < 6:
#         grayer.right(90)
#     else:
#         grayer.left(90)
#     side = side + 1
    
#method 3
for distance in [160, 40, 200, 200, 200, 40, 160, -120]:
    grayer.forward(distance)
    grayer.left(90)

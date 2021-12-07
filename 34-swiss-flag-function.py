import turtle

def draw_cross(some_turtle, side_length):
    '''Draw a cross shape, with each side being side_length long.'''
    for side in range(4):
        for i in range(3):
            some_turtle.forward(side_length)
            some_turtle.right(90)
        some_turtle.right(180)

canvas = turtle.Screen()
eason = turtle.Turtle()
eason.pensize(4)

draw_cross(eason, 150)

#william
# for i in range(4):
#     for z in range(2):
#         eason.forward(100)
#         eason.left(90)
#     eason.forward(100)
#     eason.right(90)


#max
# for i in [50, -50, -50, -50, 50, 50, 50, -50, -50, -50, 50, 50]:
#     eason.forward(i)
#     eason.left(90)


# mikhail
# for side in range(4):
#     for i in range(3):
#         eason.forward(100)
#         eason.right(90)
#     eason.right(180)


#joel
# for side in range(4):
#     eason.forward(50)
#     eason.left(90)
#     eason.forward(50)
#     eason.left(90)
#     eason.forward(50)
#     eason.right(90)
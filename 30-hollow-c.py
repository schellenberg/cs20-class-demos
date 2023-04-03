import turtle

canvas = turtle.Screen()

elaina = turtle.Turtle()
elaina.pensize(5)

#draw hollow C shape

#schellenberg's solution
for side in [170, 30, 200, 230, 200, 30, 170, 0, 0, 170]:
    elaina.forward(side)
    elaina.left(90)
    
# elaina.left(180)
# elaina.forward(170)

#tareen's solution
# elaina.right(90)
# elaina.forward(120)
# elaina.left(90)
# elaina.forward(160)
# for side in [40, 200, 200, 200, 40, 160]:
#     elaina.right(90)
#     elaina.forward(side)

#shalaine's solution
# elaina.forward(200)
# elaina.right(90)
# elaina.forward(30)
# elaina.right(90)
# elaina.forward(170)
# elaina.left(90)
# elaina.forward(170)
# elaina.left(90)
# elaina.forward(170)
# elaina.right(90)
# elaina.forward(30)
# elaina.right(90)
# elaina.forward(200)
# elaina.right(90)
# elaina.forward(230)

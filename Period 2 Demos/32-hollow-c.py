import turtle

window = turtle.Screen()
austin = turtle.Turtle()
austin.pensize(5)

#hollow c
# austin.forward(150)
# austin.left(90)
# austin.forward(50)
# austin.left(90)
# austin.forward(200)
# austin.left(90)
# austin.forward(200)
# austin.left(90)
# austin.forward(200)
# austin.left(90)
# austin.forward(50)
# austin.left(90)
# austin.forward(150)
# austin.right(90)
# austin.forward(100)
# austin.right(90)


#version 2
# for side in [150, 50, 200, 200, 200, 50, 150]:
#     austin.forward(side)
#     austin.left(90)
#     
# austin.left(180)
# austin.forward(100)


#version 3
for side in [150, 50, 200, 200, 200, 50, 150, 0, 0, 100]:
    austin.forward(side)
    austin.left(90)
    

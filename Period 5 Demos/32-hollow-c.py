import turtle

window = turtle.Screen()

seth = turtle.Turtle()
seth.pensize(5)

#version 1
# seth.forward(200)
# seth.left(90)
# seth.forward(50)
# seth.left(90)
# seth.forward(250)
# seth.left(90)
# seth.forward(350)
# seth.left(90)
# seth.forward(250)
# seth.left(90)
# seth.forward(50)
# seth.left(90)
# seth.forward(200)
# seth.left(90)
# 
# seth.left(180)
# seth.forward(250)

#version 2
# for side in [200, 50, 250, 350, 250, 50, 200]:
#     seth.forward(side)
#     seth.left(90)
#     
# seth.left(180)
# seth.forward(250)

#version 3
for side in [200, 50, 250, 350, 250, 50, 200, -250]:
    seth.forward(side)
    seth.left(90)
    
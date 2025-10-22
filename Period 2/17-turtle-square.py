import turtle

window = turtle.Screen()

anthony = turtle.Turtle()
anthony.shape("turtle")

#draw a square - kinda crappy way
# anthony.forward(200)
# anthony.left(90)
# anthony.forward(200)
# anthony.left(90)
# anthony.forward(200)
# anthony.left(90)
# anthony.forward(200)
# anthony.left(90)

#draw a square -- better way
for side in range(4):
    anthony.forward(200)
    anthony.left(90)
    
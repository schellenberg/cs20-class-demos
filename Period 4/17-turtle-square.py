import turtle

window = turtle.Screen()

mitt = turtle.Turtle()
mitt.shape("turtle")

#mitt draws a square -- kinda crappy way
# mitt.forward(200)
# mitt.left(90)
# mitt.forward(200)
# mitt.left(90)
# mitt.forward(200)
# mitt.left(90)
# mitt.forward(200)
# mitt.left(90)

#draw a square -- better way
for side in range(4):
    mitt.forward(200)
    mitt.left(360/4)

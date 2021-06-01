import turtle

# setup window and turtle
window = turtle.Screen()
arman = turtle.Turtle()

# draw a hollow c shape
for side in [250, 50, 300, 300, 300, 50, 250, -200]:
    arman.forward(side)
    arman.left(90)


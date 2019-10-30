import turtle

# set up window and turtle
window = turtle.Screen()

amy = turtle.Turtle()
amy.shape("turtle")
amy.pensize(4)

# draw the shape
for counter in range(4):
    for length in range(3):
        amy.forward(100)
        amy.right(90)
    amy.left(180)

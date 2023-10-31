import turtle

screen = turtle.Screen()
mark = turtle.Turtle()
mark.pensize(5)
mark.speed(0)

# diamond shape
mark.left(45)
for side in range(4):
    mark.forward(150)
    mark.left(90)
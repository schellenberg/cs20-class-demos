import turtle

# set up the window
canvas = turtle.Screen()
canvas.bgcolor("yellow")

# create the turtle
leah = turtle.Turtle()
leah.shape("turtle")
leah.color("blue")
leah.pensize(5)

# draw a triangle
for side in range(3):
    leah.forward(300)
    leah.left(360/3)

canvas.exitonclick()
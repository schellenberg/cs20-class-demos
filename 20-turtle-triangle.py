import turtle

#setup the window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup the turtle
prasish = turtle.Turtle()
prasish.shape("turtle")
prasish.color("blue")
prasish.pensize(10)

#draw a triangle
for side in range(3):
    prasish.forward(300)
    prasish.left(120)
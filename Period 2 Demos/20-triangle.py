import turtle

#setup screen and turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")
faith = turtle.Turtle()
faith.shape("turtle")
faith.color("red")
faith.pensize(5)

#draw a triangle
counter = 0
while counter < 3:
    faith.forward(100)
    faith.left(120)
    counter = counter + 1

canvas.exitonclick()
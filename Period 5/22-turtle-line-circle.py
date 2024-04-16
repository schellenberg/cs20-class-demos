import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

luc = turtle.Turtle()
luc.color("white")
luc.shape("turtle")
luc.pensize(8)

# draw a circle
luc.left(90)
for side in range(360):
    luc.forward(1)
    luc.left(1)

#draw the line
luc.left(90)
luc.backward(25)
luc.forward(170)

luc.hideturtle()
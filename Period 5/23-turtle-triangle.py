import turtle

canvas = turtle.Screen()
canvas.bgcolor("yellow")

audrey = turtle.Turtle()
audrey.shape("turtle")
audrey.color("pink")
audrey.pensize(5)

#make audrey draw a triangle
for side in range(3):
    audrey.forward(200)
    audrey.left(360/3)

canvas.exitonclick()
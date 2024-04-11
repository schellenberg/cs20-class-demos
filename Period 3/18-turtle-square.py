import turtle

#setup window and it's attributes
window = turtle.Screen()
window.bgcolor("yellow")

# setup turtle and it's attributes
drake = turtle.Turtle()
drake.shape("turtle")
drake.color("red")
drake.pensize(5)

# draw a square
for side in range(4):
    drake.forward(100)
    drake.left(90)

#exit the window when you click
window.exitonclick()

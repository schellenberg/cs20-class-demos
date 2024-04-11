import turtle

# setting up the window
window = turtle.Screen()
window.bgcolor("yellow")

# setting up my turtle
albert = turtle.Turtle()
albert.shape("turtle")
albert.color("green")
albert.pensize(5)

# draw a square
for side in range(4):
    albert.forward(100)
    albert.left(90)

#optional, but if you want, you can use it...
window.exitonclick()


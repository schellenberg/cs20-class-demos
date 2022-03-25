import turtle

#create window
window = turtle.Screen()
window.bgcolor("lightgreen")

#create the turtle
donteh = turtle.Turtle()
donteh.shape("turtle")
donteh.color("blue")
donteh.pensize(5)

#draw the shape
for square in range(10):
    for side in range(4):
        donteh.forward(100)
        donteh.left(90)
    donteh.left(360/10)

window.exitonclick()
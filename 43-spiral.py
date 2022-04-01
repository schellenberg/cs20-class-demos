import turtle

# setup screen
window = turtle.Screen()
window.bgcolor("black")

# setup the turtle
josh = turtle.Turtle()
josh.shape("turtle")
josh.color("white")
josh.penup()
josh.speed(0)

# draw my shape
for distance in range(5, 150, 2):
    josh.stamp()
    josh.forward(distance)
    josh.right(25)

window.exitonclick()
import turtle

window = turtle.Screen()

kyran = turtle.Turtle()
kyran.color("green")
kyran.pensize(4)
kyran.shape("turtle")
kyran.speed(0)

kyran.penup()

for movement in range(5, 200, 2):
    kyran.stamp()
    kyran.forward(movement)
    kyran.right(24)

window.exitonclick()

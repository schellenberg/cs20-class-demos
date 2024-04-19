import turtle

canvas = turtle.Screen()

jeff = turtle.Turtle()
jeff.shape("turtle")
jeff.penup()
jeff.speed(0)

for step_size in range(10, 400, 4):
    jeff.stamp()
    jeff.forward(step_size)
    jeff.left(50)

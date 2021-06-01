import turtle

# setup window
canvas = turtle.Screen()
canvas.bgcolor("black")

# setup turtle
johnson = turtle.Turtle()
johnson.shape("turtle")
johnson.color("white")
johnson.penup()
johnson.speed(0)

# draw spiral shape
for step_size in range(5, 150, 2):
    johnson.stamp()
    johnson.forward(step_size)
    johnson.left(22)
    
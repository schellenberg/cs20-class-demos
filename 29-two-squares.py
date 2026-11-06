import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightblue")

christian = turtle.Turtle()
christian.shape("turtle")
christian.color("red")
christian.pensize(5)
christian.speed(0)

#head to first square location
christian.penup()
christian.backward(300)
christian.right(90)
christian.forward(150)
christian.left(90)
christian.pendown()

#draw square
for side in range(4):
    christian.forward(200)
    christian.right(90)

#head to second square location
christian.penup()
christian.forward(400)
christian.pendown()

#draw square
for side in range(4):
    christian.forward(200)
    christian.right(90)


christian.hideturtle()

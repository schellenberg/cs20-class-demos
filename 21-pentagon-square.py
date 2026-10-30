import turtle

#setup window
easel = turtle.Screen()
easel.bgcolor("lightblue")

#setup turtle
aaron = turtle.Turtle()
aaron.shape("turtle")
aaron.color("red")
aaron.pensize(4)

ignatius = turtle.Turtle()
ignatius.shape("turtle")
ignatius.color("blue")

#move to starting spot
ignatius.penup()
ignatius.backward(250)
ignatius.pendown()

#draw pentagon with aaron
for side in range(5):
    aaron.forward(100)
    aaron.left(360/5)

#draw a square with ignatius
for side in range(4):
    ignatius.forward(100)
    ignatius.left(360/4)



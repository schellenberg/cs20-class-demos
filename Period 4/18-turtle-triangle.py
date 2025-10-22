import turtle

#set up the window
canvas = turtle.Screen()
canvas.bgcolor("lightblue")

#set up the turtle
sadeem = turtle.Turtle()
sadeem.shape("turtle")
sadeem.color("red")
sadeem.pensize(5)

#draw the triangle
for side in range(3):
    sadeem.forward(300)
    sadeem.left(360/3)

canvas.exitonclick()
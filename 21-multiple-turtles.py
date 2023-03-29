import turtle

#setup the screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setting up turtle
john = turtle.Turtle()
john.color("red")
john.shape("turtle")
john.pensize(5)

tareen = turtle.Turtle()
tareen.color("blue")
tareen.shape("turtle")
tareen.pensize(3)
tareen.penup()
tareen.backward(100)
tareen.pendown()

#draw triangle
for side in range(3):
    john.forward(150)
    john.left(360/3)
    
#draw square
for some_color in ["black", "blue", "yellow", "purple"]:
    tareen.color(some_color)
    tareen.forward(50)
    tareen.left(360/4)
    
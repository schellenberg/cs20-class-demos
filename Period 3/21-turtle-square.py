import turtle

#setting up the window
the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

#setting up the turtle
luca = turtle.Turtle()
luca.color("pink")
luca.pensize(10)

#draw a square
for side in range(4):
    luca.forward(200)
    luca.left(90)

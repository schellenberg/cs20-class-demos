import turtle

#setup window
canvas = turtle.Screen()
canvas.bgcolor("black")

#setup turtle
ivan = turtle.Turtle()
ivan.color("white")
ivan.pensize(10)

#draw a square
for the_color in ["green", "red", "yellow", "white"]:
    ivan.color(the_color)
    ivan.forward(200)
    ivan.left(360/4)
    
    
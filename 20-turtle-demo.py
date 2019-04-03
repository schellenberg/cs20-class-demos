import turtle
import easygui_qt as easy

canvas = turtle.Screen()
canvas.colormode(255)
background_color_selected = easy.get_color_rgb()
canvas.bgcolor(background_color_selected)

shane = turtle.Turtle()
shane.pensize(5)
shane.shape("turtle")
shane.color("green")

for side in range(4):
    shane.forward(100)
    shane.left(90)

#canvas.exitonclick()
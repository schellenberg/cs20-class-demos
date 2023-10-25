#draw a triangle

import turtle
import PySimpleGUI as sg

the_color = sg.popup_get_text("What colour should the background be?")

canvas = turtle.Screen()
canvas.bgcolor(the_color)

cherry = turtle.Turtle()
cherry.color("blue")
cherry.pensize(4)
cherry.shape("turtle")

for side in range(3):
    cherry.forward(200)
    cherry.left(360/3)
    
cherry.penup()
cherry.back(75)

canvas.exitonclick()
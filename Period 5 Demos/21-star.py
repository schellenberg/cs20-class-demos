#draw a star

# the width of the turtles pen
# the turtle color
# the length of the sides of the star that will be drawn
# the background color to use

import turtle
import PySimpleGUI as sg

#get user input
pen_width = sg.popup_get_text("Pen width?")
turtle_color = sg.popup_get_text("Turtle color?")
side_length = sg.popup_get_text("Side length?")
background_color = sg.popup_get_text("Background color?")

#convert data types
pen_width = int(pen_width)
side_length = int(side_length)

canvas = turtle.Screen()
canvas.bgcolor(background_color)

arthi = turtle.Turtle()
arthi.color(turtle_color)
arthi.pensize(pen_width)

for side in range(5):
    arthi.forward(side_length)
    arthi.right(720/5)

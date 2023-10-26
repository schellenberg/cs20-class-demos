# Color Selection

import turtle
import PySimpleGUI as sg

background_color = sg.popup_get_text("What's the background color? ")
brees_color = sg.popup_get_text("What's the turtle's color? ")

# create window, and set it's color
canvas = turtle.Screen()
canvas.bgcolor(background_color)

#create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color(brees_color)
bree.pensize(3)

#draw!
bree.forward(100)
bree.right(60)
bree.forward(100)

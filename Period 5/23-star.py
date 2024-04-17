import turtle
import PySimpleGUI as sg

# the width of the turtles pen
the_width = sg.popup_get_text("What width should we use for the pen? ")
the_width = int(the_width)

# the turtle color
the_color = sg.popup_get_text("What color should it be? ")

# the length of the sides of the star that will be drawn
length = sg.popup_get_text("How long should each side length be? ")
length = int(length)

# the background color to use
background_color = sg.popup_get_text("What color should the background be? ")

canvas = turtle.Screen()
canvas.bgcolor(background_color)

sajid = turtle.Turtle()
sajid.color(the_color)
sajid.pensize(the_width)


#draw the star
for side in range(5):
    sajid.forward(length)
    sajid.right(720/5)




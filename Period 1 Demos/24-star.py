import turtle
import PySimpleGUI as sg

# the width of the turtles pen
# the turtle color
# the length of the sides of the star that will be drawn
# the background color to use

#get user choices
pen_width = sg.popup_get_text("Width of the turtles pen?")
the_color = sg.popup_get_text("Color of the turtle?")
side_length = sg.popup_get_text("How long is each side?")
background_color = sg.popup_get_text("Background color?")

#convert data types
pen_width = int(pen_width)
side_length = int(side_length)

window = turtle.Screen()
window.bgcolor(background_color)

michael = turtle.Turtle()
michael.color(the_color)
michael.pensize(pen_width)

for side in range(5):
    michael.forward(side_length)
    michael.right(720/5)
    
    
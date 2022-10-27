# Color Selection

import turtle
import easygui_qt as easy

#get colors from user
the_background = easy.get_string("What color should the background be? ")
bree_color = easy.get_string("What color should the turtle be? ")

# create window, and set it's color
canvas = turtle.Screen()
canvas.bgcolor(the_background)

#create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color(bree_color)
bree.pensize(3)

#draw!
bree.forward(100)
bree.right(60)
bree.forward(100)

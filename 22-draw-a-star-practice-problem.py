# Draw a Star

import turtle

# create window and turtle
the_window = turtle.Screen()
bree = turtle.Turtle()

# get input from user
pen_width = the_window.numinput("Pen Width?", "How thick should the pen be? (1-10 recommended)")
length_of_side = the_window.numinput("Length?", "How long should each side be (in pixels)?")
turtle_color = the_window.textinput("Turtle Color?", "What color should the turtle be?")
background_color = the_window.textinput("Background Color?", "What color should the background be?")

# convert user input to integer
pen_width = int(pen_width)
length_of_side = int(length_of_side)

# set attributes of window and turtle
the_window.bgcolor(background_color)
bree.color(turtle_color)
bree.shape("turtle")
bree.pensize(pen_width)

# draw the polygon
for side in range(5):
    bree.forward(length_of_side)
    bree.right(720/5)

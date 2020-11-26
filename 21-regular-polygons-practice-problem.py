# Drawing Regular Polygons

import turtle

# create window, and set it's color
the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

# get input from user
number_of_sides = the_window.numinput("Sides?", "How many sides should the polygon have?")
length_of_side = the_window.numinput("Length?", "How long should each side be (in pixels)?")
number_of_sides = int(number_of_sides)
length_of_side = int(length_of_side)

# create the turtle, and it's attributes
bree = turtle.Turtle()
bree.color("blue")
bree.shape("turtle")
bree.pensize(3)

# draw the polygon
for side in range(number_of_sides):
    bree.forward(length_of_side)
    bree.left(360/number_of_sides)

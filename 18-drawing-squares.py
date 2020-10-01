# Create a program that uses the turtle module to draw a square.
# The user should be able to set a number of options each time the code
# runs, so the program should ask the user for:
# 
#     the width of the turtles pen
#     the turtle color
#     the length of the sides of the square that will be drawn
#     the background color to use

import turtle
import easygui_qt as ez

width = ez.get_integer("What should the width of the pen be?")
my_color = ez.get_string("What color should the turtle be?")
square_size = ez.get_integer("How long should the square be?", "Square Size", 100, 10, 400)
the_background = ez.get_string("What color should the background be?")

window = turtle.Screen()
window.bgcolor(the_background)

caleb = turtle.Turtle()
caleb.color(my_color)
caleb.pensize(width)

for side in range(4):
    caleb.forward(square_size)
    caleb.left(90)



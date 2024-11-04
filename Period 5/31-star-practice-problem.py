# Create a program that uses the turtle module to draw a five sided star. The user should be able to set a number of options each time the code runs, so the program should ask the user for:
# 
# the width of the turtles pen
# 
# the turtle color
# 
# the length of the sides of the star that will be drawn
# 
# the background color to use

import turtle

pen_width = input("How wide should the pen be? ")
pen_width = int(pen_width)
turtle_color = input("What color should the turtle be? ")
side_length = input("How long should each side be? ")
side_length = int(side_length)
background_color = input("What color should the background be? ")

window = turtle.Screen()
window.bgcolor(background_color)

nikolai = turtle.Turtle()
nikolai.color(turtle_color)
nikolai.pensize(pen_width)

for side in range(5):
    nikolai.forward(side_length)
    nikolai.right(720/5)

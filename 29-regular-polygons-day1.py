# 10.5.1. Regular Polygons
# Create a program that uses for loops to make a turtle draw regular
# polygons (regular means all sides the same lengths, all angles the same).
# First, ask the user how many sides they want the polygon to have, and how
# long each side length should be. Now draw the regular polygon that meets
# the user’s requirements!

import turtle
import easygui_qt as easy

# get user choices
number_of_sides = easy.get_int("How many sides should the polygon have?", "Number of Sides", 5)
side_length = easy.get_int("How long should the sides be?", "Side Length", 100, 10, 300)

# setup window
window = turtle.Screen()
window.bgcolor("green")

# setup turtle
ali = turtle.Turtle()
ali.color("blue")
ali.shape("turtle")
ali.pensize(5)

# draw polygon
for side in range(number_of_sides):
    ali.forward(side_length)
    ali.left(360/number_of_sides)


# 9.5.2. Drawing any Size of Square Practice Problem
# from https://cs20.ca/Python/Overview/FirstTurtleProgram.html#practice-problems
# Create a program that uses the turtle module to draw a square. The user should be able to set a
# number of options each time the code runs, so the program should ask the user for:

# the width of the turtles pen
# the turtle color
# the length of the sides of the square that will be drawn
# the background color to use

# Hint: your input from the user will return a string, but the turtles pensize method expects its
# argument to be an int. That means you need to convert the string to an int before you pass it to pensize.

import turtle

# get the options from the user
pen_width = input("What should the width of the pen be? ")
turtle_color = input("What color should the turtle be? ")
side_length = input("How long should each side be? ")
background_color = input("What should the background color be? ")

# convert data types, for input that should be numbers
pen_width = int(pen_width)
side_length = int(side_length)

# set up the screen
window = turtle.Screen()
window.bgcolor(background_color)

# set up the turtle
michelle = turtle.Turtle()
michelle.color(turtle_color)
michelle.pensize(pen_width)

# draw the square
for side in range(4):
    michelle.forward(side_length)
    michelle.left(90)


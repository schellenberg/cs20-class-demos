## 9.5.2. Drawing any Size of Square
# Create a program that uses the turtle module to draw a square. The user should be able to set a number of options each time the code runs, so the program should ask the user for:
# the width of the turtles pen# 
# the turtle color# 
# the length of the sides of the square that will be drawn
#  the background color to use# 

import easygui_qt as easy
import turtle

width = easy.get_integer("How wide should the pen be?")
the_color = easy.get_string("What color should the turtle be?")
side_length = easy.get_integer("How long should each side be?")
background = easy.get_string("What color should the background be?")

window = turtle.Screen()
window.bgcolor(background)

leshane = turtle.Turtle()
leshane.color(the_color)
leshane.pensize(width)


#for loop
for side in range(4): #range(4) makes a list -> [0,1,2,3]
    leshane.forward(side_length)
    leshane.left(90)


#while loop
# sides = 0
# while sides < 4:
#     leshane.forward(side_length)
#     leshane.left(90)
#     sides = sides + 1

# not using a loop
# leshane.forward(side_length)
# leshane.left(90)
# leshane.forward(side_length)
# leshane.left(90)
# leshane.forward(side_length)
# leshane.left(90)
# leshane.forward(side_length)
# leshane.left(90)

# draw a star

# ask the user for the following:
#     the width of the turtles pen
#     the turtle color
#     the length of the sides of the star that will be drawn
#     the background color to use

import turtle
import easygui_qt as easy

width = easy.get_integer("What's the width of the pen?")
zain_color = easy.get_string("What color should Zain be?")
star_length = easy.get_integer("How long should the sides be?")
background_color = easy.get_string("What should the background color be?")

window = turtle.Screen()
window.bgcolor(background_color)

zain = turtle.Turtle()
zain.color(zain_color)
zain.pensize(width)

#draw the star
for side in range(5):
    zain.forward(star_length)
    zain.right(720/5)




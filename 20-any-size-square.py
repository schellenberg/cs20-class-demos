import turtle
import easygui_qt as easy

window = turtle.Screen()

# the background color to use
back_color = easy.get_string("What background color do you want?")
window.bgcolor(back_color)

remi = turtle.Turtle()

# the width of the turtles pen
width = easy.get_integer("How wide should the pen be?")
remi.pensize(width)

# the turtle color
remi_color = easy.get_string("What color should the turtle be?")
remi.color(remi_color)

# the length of the sides of the square that will be drawn
length = easy.get_integer("How long should each side be?")

for side in range(4):
    remi.forward(length)
    remi.left(90)

import turtle
import easygui_qt as easy

window = turtle.Screen()

obi = turtle.Turtle()
obi.shape("turtle")

obi_color = easy.get_string("What color should we use?")
obi.color(obi_color)

pen_width = easy.get_integer("How wide should the line be?")
obi.pensize(pen_width)

side_length = easy.get_integer("How long should each side be?")

for side in range(8):
    obi.forward(side_length)
    obi.left(360/8)
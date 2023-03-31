import turtle
import easygui_qt as easy

canvas = turtle.Screen()
benett = turtle.Turtle()
benett.pensize(4)

number_of_sides = easy.get_integer("How many sides?")
side_length = easy.get_integer("How long should the sides be?")

for side in range(number_of_sides):
    benett.forward(side_length)
    benett.left(360/number_of_sides)

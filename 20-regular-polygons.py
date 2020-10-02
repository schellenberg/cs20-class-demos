import turtle
import easygui_qt as easy

sides = easy.get_integer("How many sides should the polygon have?")
side_length = easy.get_integer("How long should each side be?")

window = turtle.Screen()
aiden = turtle.Turtle()
aiden.pensize(3)

for side in range(sides):
    aiden.forward(side_length)
    aiden.left(360/sides)
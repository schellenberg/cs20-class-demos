import turtle
import easygui_qt as easy

canvas = turtle.Screen()
liam = turtle.Turtle()
liam.shape("turtle")
liam.pensize(5)

number_of_sides = easy.get_integer("How many sides?", "Sides", 5, 3, 15)
side_length = easy.get_integer("How long should the sides be?", "Length", 100, 20, 300)

for side in range(number_of_sides):
    liam.forward(side_length)
    liam.left(360/number_of_sides)
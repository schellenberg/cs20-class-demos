import turtle
import easygui_qt as easy

number_of_sides = easy.get_int("How many sides do you want the polygon to have?")
side_length = easy.get_int("How long should each side be?")

canvas = turtle.Screen()
canvas.bgcolor("black")

quinten = turtle.Turtle()
quinten.shape("turtle")
quinten.color("red")
quinten.pensize(5)

# draw the polygon
for side in range(number_of_sides):
    quinten.forward(side_length)
    quinten.left(360/number_of_sides)

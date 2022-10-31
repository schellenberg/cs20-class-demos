import turtle
import easygui_qt as easy

window = turtle.Screen()
eli = turtle.Turtle()
eli.shape("turtle")
eli.color("orange")
eli.pensize(5)

number_of_sides = easy.get_integer("How many sides should there be?", "Sides", 5, 3, 15)
side_length = easy.get_integer("How long should the sides be?", "Side Length", 100, 25, 300)

for side in range(number_of_sides):
    eli.forward(side_length)
    eli.left(360/number_of_sides)

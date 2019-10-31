import turtle
import easygui_qt as easy

canvas = turtle.Screen()
canvas.bgcolor("black")

ethan = turtle.Turtle()
ethan.shape("turtle")
ethan.color("red")
ethan.pensize(5)

joseph = turtle.Turtle()
joseph.shape("turtle")
joseph.color("blue")
joseph.pensize(3)

side_length = easy.get_integer("How long should each side length be?", "Side length", 100, 25, 400)
for some_color in ["purple","green","yellow"]:
    ethan.color(some_color)
    ethan.forward(side_length)
    ethan.left(360/3)

joseph.backward(75)

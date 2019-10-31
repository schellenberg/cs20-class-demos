import turtle
import easygui_qt as easy

window = turtle.Screen()
background_color = easy.get_string("What color should the background be?")
window.bgcolor(background_color)

filiz = turtle.Turtle()
filiz.shape("turtle")
width = easy.get_integer("How wide should the pen be?")
filiz.pensize(width)
filiz_color = easy.get_string("What color should the turtle be?")
filiz.color(filiz_color)

side_length = easy.get_integer("How long should the sides be?", "Side length", 150, 50, 400)
for side in range(5):
    filiz.forward(side_length)
    filiz.right(720/5)
import turtle
import easygui_qt as easy

canvas = turtle.Screen()
background = easy.get_string("What color should the background be?")
canvas.bgcolor(background)

sam = turtle.Turtle()
sam_color = easy.get_string("What color should your turtle be?")
sam.color(sam_color)
sam.shape("turtle")
width = easy.get_integer("How wide should the pen be?")
sam.pensize(width)

side_length = easy.get_integer("How long should each side be?", "Side length", 100, 50, 400)
for side in range(5):
    sam.forward(side_length)
    sam.right(720/5)

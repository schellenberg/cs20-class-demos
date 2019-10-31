import turtle
import easygui_qt as easy

canvas = turtle.Screen()
canvas.bgcolor("yellow")

michael = turtle.Turtle()
michael.shape("turtle")
michael.color("red")
michael.pensize(5)

ray = turtle.Turtle()
ray.color("blue")
ray.pensize(25)

side_length = easy.get_integer("How large should each side be?", "Side length", 100, 50, 400)
for some_color in ["green", "black", "blue"]:
    michael.color(some_color)
    michael.forward(side_length)
    michael.left(120)
    
ray.backward(300)
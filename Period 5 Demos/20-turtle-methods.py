# draw me a pentagon (5 sided shape)
import turtle
import PySimpleGUI as sg

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

katie = turtle.Turtle()
katie.color("blue")
katie.pensize(5)
katie.shape("turtle")

for side in range(5):
    katie.forward(100)
    katie.left(360/5)

katie.penup()
katie.backward(100)

canvas.exitonclick()

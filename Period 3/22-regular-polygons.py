import turtle
import PySimpleGUI as sg

number_of_sides = sg.popup_get_text("How many sides should there be? ")
length_of_side = sg.popup_get_text("How long should each side be? ")

window = turtle.Screen()
oleksandra = turtle.Turtle()

number_of_sides = int(number_of_sides)
length_of_side = int(length_of_side)

for side in range(number_of_sides):
    oleksandra.forward(length_of_side)
    oleksandra.left(360/number_of_sides)
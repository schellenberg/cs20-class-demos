import turtle
import PySimpleGUI as sg

#get user choices
side_number = sg.popup_get_text("How many sides?")
side_length = sg.popup_get_text("How long is each side?")

#convert data types
side_number = int(side_number)
side_length = int(side_length)

window = turtle.Screen()
michael = turtle.Turtle()

for side in range(side_number):
    michael.forward(side_length)
    michael.left(360/side_number)
    
    
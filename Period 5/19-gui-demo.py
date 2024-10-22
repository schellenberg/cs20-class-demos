import FreeSimpleGUI as sg

name = sg.popup_get_text("What's your name? ")
age = sg.popup_get_text("How old are you? ")

greeting = f"Hey there, {name}! You're already {age} years old!"
sg.popup(greeting)

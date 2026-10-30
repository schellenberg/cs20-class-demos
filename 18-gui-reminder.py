import FreeSimpleGUI as sg

name = sg.popup_get_text("What's your name?")

greeting = f"Hello there, {name}!"
sg.popup(greeting)
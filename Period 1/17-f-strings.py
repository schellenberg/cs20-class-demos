import FreeSimpleGUI as sg

first_name = sg.popup_get_text("What's your first name?")
last_name = sg.popup_get_text("What's your last name?")

greeting = f"Hello there, {first_name} {last_name}!"
sg.popup(greeting)
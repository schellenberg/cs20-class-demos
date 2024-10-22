import FreeSimpleGUI as sg

age = sg.popup_get_text("How old are you?")
age = int(age)
if age > 15:
    sg.popup(f"Wow! Already {age} years old!")

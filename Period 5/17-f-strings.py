import FreeSimpleGUI as sg

name = sg.popup_get_text("What's your name?")
team = sg.popup_get_text("Who's going to win March Madness?")

if team == "Duke":
    sg.popup(f"Yup, I agree {name}. I think {team} are going to win!")

else:
    sg.popup(f"Uh oh, {name}. I don't think {team} are going to win!")
    
    
import easygui_qt as easy

name = easy.get_string("What's your name?")

if name == "Elijah" or name == "Saad":
    message = f"Welcome here, {name}!"
    easy.show_message(message)
    
else:
    message = f"Go away please, {name}!"
    easy.show_message(message)
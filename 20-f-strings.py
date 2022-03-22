import easygui_qt as easy

name = easy.get_string("What's your name?")
age = easy.get_integer("How old are you?")

message = f"Hey there, {name}. You are {age} years old."
easy.show_message(message)
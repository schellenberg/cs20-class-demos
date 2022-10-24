import easygui_qt as easy

name = easy.get_string("Who are you? ")
age = easy.get_integer("How old are you? ")

reply = f"Hello there, {name}! I hear you are {age} years old!"
easy.show_message(reply)
import easygui_qt as easy

name = easy.get_string("What's your name? ")
age = easy.get_int("How old are you?")

easy.show_message("Hello there, " + name)
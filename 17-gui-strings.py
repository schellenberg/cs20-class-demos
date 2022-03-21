import easygui_qt as easy

name = easy.get_string("What's your name?")

greeting = "Hello there " + name + "!"
easy.show_message(greeting, "Well hi!")
import easygui_qt as easy

name = easy.get_string("What is your name?")
age = easy.get_integer("How old are you?")

courses = ["Physics", "Pre-Calc", "Photo", "Physical Science", "Psychology", "Comp Sci"]
favourite = easy.get_choice("What's your fav?", "Subject", courses)

easy.show_message(f"Hello there, {name}!")
easy.show_message(f"I hear you are {age} years old.")
easy.show_message(f"Yeah, {favourite}  is really fun.")
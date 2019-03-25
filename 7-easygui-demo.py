import easygui_qt as easy

first_name = easy.get_string("Please enter your first name")
last_name = easy.get_string("Please enter your last name")

age = easy.get_integer("Please enter your age")

greeting = f"Hello there, {first_name} {last_name}! You're already {age} years old."

easy.show_message(greeting)

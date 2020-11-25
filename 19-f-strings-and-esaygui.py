import easygui_qt as easy

name = easy.get_string("What's your name?")
age = easy.get_int("How old are you?")

greeting = f'''Hello, {name}.

I heard you just turned {age}!'''

easy.show_message(greeting)


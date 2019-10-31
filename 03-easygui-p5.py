import easygui_qt as easy

age = easy.get_integer("How old are you?")

if age > 15:
    greeting = "Wow! Already " + str(age) + " years old!"
    easy.show_message(greeting)

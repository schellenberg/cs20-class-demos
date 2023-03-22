import easygui_qt as easy

age = easy.get_integer("How old are you?", "Age", 15, 0, 130)

if age > 15:
    easy.show_message(f"Wow! Already {age} years old!", "Age")

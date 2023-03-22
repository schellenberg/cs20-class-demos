import easygui_qt as easy

subjects = ["Math", "Guitar", "Health Science", "Biology", "Computer Science", "English"]
fav = easy.get_choice("Pick your fav class", "Classes", subjects)

if fav == "Guitar":
    easy.show_message("Sounds fun!")
elif fav == "Math":
    easy.show_message("That's a good sine!")

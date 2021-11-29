import easygui_qt as easy

tv_shows = ["Community", "Survivor", "Stranger Things", "Chainsaw Man"]

name = easy.get_string("What's your name? ")
age = easy.get_integer("How old are you?")
fav = easy.get_choice("Pick your fave!", "Pick fave", tv_shows)

if fav == "Community":
    easy.show_message("Cool cool cool...")
elif age >= 16:
    easy.show_message("You can drive, " + name)
elif name == "Obi":
    easy.show_message("Hey there, Obi!")
else:
    easy.show_message("Hello there " + name)
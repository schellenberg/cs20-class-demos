import easygui_qt as easy

#name = easy.get_string("What's you name?")
#age = easy.get_integer("How old are you?")

#subjects = ["English", "Math", "Band", "Enviro Sci", "History"]
#favourite = easy.get_choice("What's your fav?", "Please pick", subjects)

happy = easy.get_yes_or_no("Are you happy?")

if happy == True:
    easy.show_message("Glad to hear it!")
else:
    easy.show_message("Uh oh. Hope you're doing better soon.")


#easy.show_message(f"Wow, {name}! You are already {age} years old!")
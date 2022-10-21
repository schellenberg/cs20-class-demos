import easygui_qt as easy

subjects = ["Foods", "Japanese", "English", "Math", "CS", "Electronics", "History"]
favourite = easy.get_choice("What's your fav?", "Pick Subject", subjects)

if favourite == "History":
    response = f"You are not doomed to repeat the past..."
    easy.show_message(response)

elif favourite == "Math":
    response = f"That's a good sine!"
    easy.show_message(response)

else:
    response = f"Good call. {favourite} is a fun class!"
    easy.show_message(response)
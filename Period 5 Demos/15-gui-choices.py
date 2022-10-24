import easygui_qt as easy

subjects = ["Math", "Physical Science", "Mechanics", "Sewing", "Accounting", "CS", "Health Science"]
favourite = easy.get_choice("Pick your fav", "Fav Class", subjects)

if favourite == "Mechanics":
    message = "Can you change my oil?"
    easy.show_message(message)
    
elif favourite == "Math":
    message = "That's a good sine!"
    easy.show_message(message)
    
else:
    message = f"Good one. {favourite} is a fun class!"
    easy.show_message(message)
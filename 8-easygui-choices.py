import easygui_qt as easy

teams = ["Duke", "Wisconsin", "North Carolina", "USC"]

winner = easy.get_choice("Who do you think will win?", "March Madness", teams)

if winner == "Duke":
    easy.show_message("Yeah. I'm pretty sure Duke is going win too!")
    
else:
    easy.show_message("I dunno. " + winner + " seems a bit unlikely...")
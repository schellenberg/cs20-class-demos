import easygui_qt as easy

winner = easy.get_string("Who's going to win the NBA playoffs?")

if winner == "":
    print("Hey! Pick somebody!")

elif winner == "Warriors":
    print("I mean, maybe...")


def will_win(team):
    if team == "Celtics" or team == "Nuggets":
        return True
    else:
        return False
    
your_team = input("Who's your team in NBA playoffs? ")
if will_win(your_team):
    print("Yup, they have a good chance!")
else:
    print("Uhhh... good luck!")
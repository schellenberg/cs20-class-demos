# Dan Schellenberg
# Simple Password Demo
# Mar 13, 2020

password = "Schellenberg"
their_guess = input("What is the password? ")
class = input("What class are you in?")

if their_guess == password:
    print(their_guess + " IS the password! Rainbows are nice!")
else:
    print(their_guess + " IS NOT the password! Get outta here!")
    
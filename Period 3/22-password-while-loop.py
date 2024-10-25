the_password = "Comp Sci"
user_guess = input("What's the password? ")

while the_password != user_guess:
    print("Hey! That wasn't the password!")
    user_guess = input("What's the password? ")

print("Welcome to the super secret area!")
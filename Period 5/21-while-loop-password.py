got_password = False
password = "hat"

while not got_password:
    user_guess = input("What's the password? ")
    if user_guess == password:
        got_password = True
    else:
        print("Hey! That wasn't the password!")
    
print("Super secret info here...")

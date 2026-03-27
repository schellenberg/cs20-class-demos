needs_password = True
while needs_password:
    guess = input("What's the password? ")
    if guess == "sask":
        needs_password = False

print("What a great place!")
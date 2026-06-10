still_asking = True

# Keep asking until the correct password is entered.
while still_asking:
    password = input("Enter the password: ")
    if password == "sask":
    # A correct password ends the loop.
        still_asking = False

# This message only appears after the password has been entered correctly.
print("What a great place!")
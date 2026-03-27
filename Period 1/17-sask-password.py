# Write a program that asks the user to enter a password.
# Keep asking for the password until they enter “sask”.
#Once they have successfully typed in “sask”,
#print out What a great place!.

still_needs_password = True
while still_needs_password:
    guess = input("What's the password? ")
    if guess == "sask":
        still_needs_password = False

print("What a great place!")
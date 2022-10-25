#Write a program that asks the user to enter a password.
#Keep asking for the password until they enter “sask”.
#Once they have successfully typed in “sask”,
#print out What a great place!.

guess = ""
while guess != "sask":
    guess = input("What's the password? ")

print("What a great place!")
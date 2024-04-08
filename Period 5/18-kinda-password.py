#Write a program that asks the user to enter a password. Keep asking for the password until they enter “sask”. Once they have successfully typed in “sask”, print out What a great place!.

password = input("What's the password? ")
while password != "sask":
    print("Nope. That's not it! Try again!")
    password = input("What's the password? ")
print("What a great place!")
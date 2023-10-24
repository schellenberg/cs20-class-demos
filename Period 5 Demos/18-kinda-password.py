# Write a program that asks the user to enter
#a password. Keep asking for the password
#until they enter “sask”. Once they have
#successfully typed in “sask”, print out
#What a great place!.

user_entry = input("What's the password? ")
while user_entry != "sask":
    print("Nope...")
    user_entry = input("What's the password? ")
    
print("What a great place! [despite snow]")
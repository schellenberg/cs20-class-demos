# Write a program that asks the user to enter a password.
# Keep asking for the password until they enter “sask”.
# Once they have successfully typed in “sask”, print out
# What a great place!.

password = ""

while password != "sask":
    password = input("Please enter the password: ")
    
print("What a great place!")
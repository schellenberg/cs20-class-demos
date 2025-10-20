#count from 1 to 100
# counter = 1
# while counter < 101:
#     print(counter)
#     counter = counter + 1


#counts down from 20 to 1, then prints Blastoff!.
# counter = 20
# while counter > 0:
#     print(counter)
#     counter = counter - 1
# print("Blastoff!")

#Write a program that asks the user to enter a password. Keep asking for the password until they enter “sask”. Once they have successfully typed in “sask”, print out What a great place!.
still_looking_for_password = True
while still_looking_for_password:
    password = input("What's the password? ")
    if password == "sask":
        still_looking_for_password = False

print("What a great place!")





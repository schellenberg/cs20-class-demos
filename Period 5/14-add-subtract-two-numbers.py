# Add/Subtract Two Numbers
# Dan Schellenberg
# March 18, 2025

# get info from the user
add_or_subtract = input("Should I add or subtract? ")
number_one = input("What's the first number? ")
number_two = input("What's the second number? ")

#convert to numbers
number_one = int(number_one)
number_two = int(number_two)

#handle addition
if add_or_subtract == "add":
    answer = number_one + number_two
    print(answer)

#handle subtraction
elif add_or_subtract == "subtract":
    answer = number_one - number_two
    print(answer)

#catch errors
else:
    print("Hey! That wasn't add or subtract!")
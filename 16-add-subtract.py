# Add/Subtract Two Numbers
# Dan Schellenberg
# Mar 18, 2022

# let user decide if adding or subtracting
add_or_subtract = input("Do you want to add or subtract? ")

# take in the two numbers
first_number = input("What's the first number? ")
second_number = input("What's the second number? ")

# convert data types
first_number = int(first_number)
second_number = int(second_number)

# do the math
if add_or_subtract == "add":
    answer = first_number + second_number

elif add_or_subtract == "subtract":
    answer = first_number - second_number

else:
    answer = "That's not add OR subtract!"

# print the result
print(answer)
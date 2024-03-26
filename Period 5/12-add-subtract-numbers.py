# Add/Subtract Two Numbers
# Dan Schellenberg
# March 26, 2024

# ask if we should add or subtract
operation = input("Do you want to add or subtract? ")

# take in the two numbers
number_one = input("What's the first number? ")
number_two = input("What's the second number? ")

# convert data types
number_one = float(number_one)
number_two = float(number_two)

# do the math
if operation == "add":
    answer = number_one + number_two

elif operation == "subtract":
    answer = number_one - number_two

else:
    answer = "unknown. Please type add or subtract."

# print the result
print("The answer is " + str(answer))


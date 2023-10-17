# Write a program that can either add or subtract two numbers.
# You should first ask the user whether they want to add or subtract,
# then take in the two numbers, then finally perform the required
# operation and print the result.

# get user input
operation = input("Do you want to add or subtract? ")
first_number = input("What's the first number? ")
second_number = input("What's the second number? ")

# convert data types
first_number = float(first_number)
second_number = float(second_number)

# add/subract
if operation == "add":
    answer = first_number + second_number

elif operation == "subtract":
    answer = first_number - second_number

else:
    answer = "undefined. That wasn't add OR subtract!"

# print the result
print("The answer is " + str(answer))


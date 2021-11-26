# Add/Subtract Two Numbers
# Dan Schellenberg
# Nov 26, 2021

# first ask the user whether they want to add or subtract
operation = input("Do you want to add or subtract? ")

# take in the two numbers
first_number = input("What's the first number? ")
second_number = input("What's the second number? ")

# convert data types
first_number = float(first_number)
second_number = float(second_number)

# perform the required operation
if operation == "add":
    answer = first_number + second_number
elif operation == "subtract":
    answer = first_number - second_number
else:
    print("Error. That wasn't an option")
    
# print the result
print("The answer is " + str(answer))
# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 18, 2024
#
# Write a program that can either add or
# subtract two numbers. You should first
# ask the user whether they want to add or
# subtract, then take in the two numbers, then
# finally perform the required operation and
# print the result.

#ask the user whether they want to add or subtract
operation = input("Do you want to add or subtract? ")

#take in the numbers
number_one = input("What's the first number? ")
number_two = input("What's the second number? ")

#convert numbers to float data type
number_one = float(number_one)
number_two = float(number_two)

#calculate the answer
if operation == "add":
    answer = number_one + number_two
    print("The answer is " + str(answer))
    
elif operation == "subtract":
    answer = number_one - number_two
    print("The answer is " + str(answer))
    
else:
    print("Hey! That wasn't add or subtract! No go.")
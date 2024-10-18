# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 18, 2024

# get the operation from user
operation = input("Do you want to add or subtract? ")

# take in both numbers
number_one = input("What's the first number? ")
number_two = input("What's the second number? ")

# convert numbers to floats
number_one = float(number_one)
number_two = float(number_two)

# do the math, and print result
if operation == "add":
    answer = number_one + number_two
    print("The answer is " + str(answer))
    
elif operation == "subtract":
    answer = number_one - number_two
    print("The answer is " + str(answer))
    
else:
    print("Hey! That wasn't add or subtract! Try again.")
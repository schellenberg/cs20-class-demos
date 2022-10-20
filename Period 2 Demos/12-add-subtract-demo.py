#get user input
operation = input("Do you want to add or subtract? ")

number_one = input("What's the first number? ")
number_two = input("What's the second number? ")

#convert data types
number_one = int(number_one)
number_two = int(number_two)

#do the math
if operation == "add":
    answer = number_one + number_two
    print("The sum is " + str(answer))
    
elif operation == "subtract":
    answer = number_one - number_two
    print("The difference is " + str(answer))
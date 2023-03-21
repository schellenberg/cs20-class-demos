# Add/Subtract Two Numbers
# Dan Schellenberg
# March 21, 2023

#get which operation to do
operation = input("Do you want to add or subtract? ")

if operation == "add":
    #get the numbers
    number_one = input("What's the first number? ")
    number_two = input("What's the second number? ")

    #convert data types
    number_one = int(number_one)
    number_two = int(number_two)

    #do the math
    answer = number_one + number_two
    
    #output the answer
    print(f"{number_one} plus {number_two} equals {answer}")

if operation == "subtract":
    #get the numbers
    number_one = input("What's the first number? ")
    number_two = input("What's the second number? ")

    #convert data types
    number_one = int(number_one)
    number_two = int(number_two)

    #do the math
    answer = number_one - number_two
    
    #output the answer
    print(f"{number_one} minus {number_two} equals {answer}")
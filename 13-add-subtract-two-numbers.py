# Add/Subtract Two Numbers
# Dan Schellenberg
# Oct 21, 2026

operation = input("Do you want to add or subtract? ")

if operation == "add":
    #get the numbers
    first_number = input("What's the first number? ")
    second_number = input("What's the second number? ")
    
    #convert data types
    first_number = int(first_number)
    second_number = int(second_number)
    
    #do math and print result
    answer = first_number + second_number
    print("If you add those, you get " + str(answer))

elif operation == "subtract":
    #get the numbers
    first_number = input("What's the first number? ")
    second_number = input("What's the second number? ")
    
    #convert data types
    first_number = int(first_number)
    second_number = int(second_number)
    
    #do math and print result
    answer = first_number - second_number
    print("If you subtract those, you get " + str(answer))
    
else:
    print("Hey! That's not add OR subtract!")
# Add/subtract demo

operator = input("Do you want to add or subtract? ")

if operator == "add":
    first_number = input("What's the first number? ")
    second_number = input("What's the second number? ")
    
    first_number = int(first_number)
    second_number = int(second_number)
    
    answer = first_number + second_number
    
    print("When you add the numbers, you get", answer)

elif operator == "subtract":
    first_number = input("What's the first number? ")
    second_number = input("What's the second number? ")
    
    first_number = int(first_number)
    second_number = int(second_number)
    
    answer = first_number - second_number
    
    print("When you subtract the numbers, you get", answer)

else:
    print("That's not a thing. Please type add or subtract.")
    
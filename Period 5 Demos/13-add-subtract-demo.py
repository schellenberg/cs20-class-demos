#get user input
operator = input("Do you want add or subtract? ")
number_one = input("First number? ")
number_two = input("Second number? ")

#convert data types
number_one = int(number_one)
number_two = int(number_two)

#do the math
if operator == "add":
    answer = number_one + number_two
    print("The sum is " + str(answer))
    
elif operator == "subtract":
    answer = number_one - number_two
    print("The difference is " + str(answer))
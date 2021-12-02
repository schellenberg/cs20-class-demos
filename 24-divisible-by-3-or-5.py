number = input("What number? ")
number = int(number)

if number % 3 == 0 or number % 5 == 0:
    print("It's divisible by 3 or 5!")
else:
    print("Not divisible by 3 or 5.")
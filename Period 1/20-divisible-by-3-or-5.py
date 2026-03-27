number = input("What's the number? ")
number = int(number)

if number % 3 == 0 or number % 5 == 0:
    print("That number is divisible by 3 or 5")
else:
    print("That number is not divisible by 3 or 5")
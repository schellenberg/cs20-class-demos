number = input("What number should I check? ")
number = int(number)

if number % 3 == 0 or number % 5 == 0:
    print("That number is divisible by either 3 or 5")

else:
    print("That number is NOT divisible by either 3 or 5")

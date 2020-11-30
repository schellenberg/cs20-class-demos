# 11.3.1. Under 100
# Write a program that takes in a number from the user,
# and correctly prints either “That number is between 1 to 100” or
# “That number is not between 1 to 100”.
# You may only use a single if/else block to solve this problem.

number = input("What number are you thinking of? ")
number = int(number)

if number >= 1 and number <= 100:
    print("The number is between 1 and 100")

else:
    print("The number is NOT between 1 and 100")

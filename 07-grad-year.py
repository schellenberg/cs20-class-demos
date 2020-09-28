# take input from user
current_year = input("What is the current year? ")
grad_year = input("What year will you graduate? ")

# convert input into integers
current_year = int(current_year)
grad_year = int(grad_year)

# do the math, and print result
year_difference = grad_year - current_year
print("You will graduate in", year_difference, "years.")
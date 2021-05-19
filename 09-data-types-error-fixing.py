# get user input
current_year = input("What is the current year? ")
grad_year = input("What year are you graduating? ")

# convert data types
current_year = int(current_year)
grad_year = int(grad_year)

# calculate
year_difference = grad_year - current_year

# output the result
print("You will graduate in " + str(year_difference) + " years.")

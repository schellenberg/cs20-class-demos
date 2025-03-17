# get the years from the user
current_year = input("What's the current year? ")
grad_year = input("What you do you graduate? ")

# converting data types
current_year = int(current_year)
grad_year = int(grad_year)

# calculating the answer
how_long = grad_year - current_year

# printing the result
print("You will graduate in " + str(how_long) + " years!")
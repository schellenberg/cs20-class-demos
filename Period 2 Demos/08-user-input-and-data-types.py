# take user input
current_year = input("What is the current year? ")
grad_year = input("What you do you graduate? ")

# convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#do the math
year_difference = grad_year - current_year

#print the result
print("You'll graduate in " + str(year_difference) + " years.")


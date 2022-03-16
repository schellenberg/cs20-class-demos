#get user input
year = input("What's the current year? ")
grad_year = input("What year do you graduate? ")

# convert to integers
year = int(year)
grad_year = int(grad_year)

#calcuate and output
year_difference = grad_year - year
print("You'll graduate in " + str(year_difference) + " years")
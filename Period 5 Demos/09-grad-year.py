# get user input
current_year = input("What year is it? ")
grad_year = input("What year do you graduate? ")

#convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#do math
year_difference = grad_year - current_year

#print result
print("You'll graduate in " + str(year_difference) + " years")

#get the year info
current_year = input("What's the current year? ")
grad_year = input("What year do you graduate? ")

#convert to numbers
current_year = int(current_year)
grad_year = int(grad_year)

#do the math
year_difference = grad_year - current_year
year_difference = str(year_difference)

#print the result
print("You will graduate in " + year_difference + " years.")


current_year = input("What's the current year? ")
grad_year = input("What year do you graduate? ")

current_year = int(current_year)
grad_year = int(grad_year)

year_difference = grad_year - current_year

print("You will graduate in " + str(year_difference) + " years.")
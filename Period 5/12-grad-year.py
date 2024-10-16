# get years from user
current_year = input("What year is it now? ")
grad_year = input("What year do you graduate? ")

# convert to numbers
current_year = int(current_year)
grad_year = int(grad_year)

# do the math
years_until_grad = grad_year - current_year

# print out the message
print("You will graduate in " + str(years_until_grad) + " years")


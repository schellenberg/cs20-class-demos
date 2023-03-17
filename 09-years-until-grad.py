# get input from user
current_year = input("What is the current year? ")
grad_year = input("What year do you graduate? ")

#convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#do the math
years_until_grad = grad_year - current_year

#print a nice message
print("You will graduate in " + str(years_until_grad) + " years")


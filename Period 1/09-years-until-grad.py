#Years Until Grad
#Mar 17/26
#Dan Schellenberg

#get user input
current_year = input("What's the current year? ")
grad_year = input("What year do you graduate? ")

#convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#doing the math
years_until_grad = grad_year - current_year

#output statement
print("Years until graduation: " + str(years_until_grad))

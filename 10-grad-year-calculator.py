# Grad Year Calculator
# Dan Schellenberg
# Oct 16, 2027

#getting info
current_year = input("What is the current year? ")
grad_year = input("What year do you graduate? ")

#convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#do the math
years_til_grad = grad_year - current_year

print("You will graduate in " + str(years_til_grad) + " years")


# Grad Time
# Dan Schellenberg
# Oct 13, 2023

# getting user input
current_year = input("What is the current year? ")
grad_year = input("What year do you graduate? ")

# convert input into numbers
current_year = int(current_year)
grad_year = int(grad_year)

# math
how_long = grad_year - current_year

# giving the user a message
print("You graduate in " + str(how_long) + " years")





# Grad Year
# Dan Schellenberg
# Oct 13, 2023

# taking user input
year_now = input("What is the current year? ")
grad_year = input("What year do you graduate? ")

# converting data types
year_now = int(year_now)
grad_year = int(grad_year)

# math
how_long = grad_year - year_now

# outputing a statement
print("You will graduate in " + str(how_long) + " years!")



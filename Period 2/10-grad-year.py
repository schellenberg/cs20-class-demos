# get info from user
current_year = input("What's the current year? ")
grad_year = input("What year do you graduate? ")

# convert data types
current_year = int(current_year)
grad_year = int(grad_year)

# do the math
year_difference = grad_year - current_year

# print the answer
print("Years until graduation: " + str(year_difference))
# get user input
name = input("What's your name? ")
fav_class = input("What's your favourite class? ")
current_year = input("What year is it now? ")
grad_year = input("What year do you graduate? ")

# convert data types
grad_year = int(grad_year)
current_year = int(current_year)

# do the math
years_until_grad = grad_year - current_year

# print a nice reply
print(name + " will graduate in " + str(years_until_grad) + " years!")


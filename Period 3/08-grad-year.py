#get user input
name = input("What's your name? ")
fav_class = input("What's your favourite class? ")
current_year = input("What's the year now? ")
grad_year = input("What year do you graduate? ")

#convert data types
current_year = int(current_year)
grad_year = int(grad_year)

#do the math calculations
years_until_grad = grad_year - current_year

#print the result
print(name + " will graduate in " + str(years_until_grad) + " years")


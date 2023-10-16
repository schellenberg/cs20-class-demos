# get user input
name = input("Tell me your name: ")
age = input("How old are you? ")

# either be nice or be mean
if name != "Muneeb":
    print("Welcome here!")

else:
    print("Go away!")

# convert data types
age = int(age)

#how old in the year 2030?
new_age = age + 7
print("You will be " + str(new_age) + " in the year 2030")

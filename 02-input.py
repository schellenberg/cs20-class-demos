name = input("Who are you? ")
age = input("How old are you? ")

# convert age from string to integer
age = int(age)

if age >= 16:
    print("You can already drive, " + name)

else:
    print("Stay off the road, " + name)
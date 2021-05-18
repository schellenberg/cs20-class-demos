#get the user's age
age = input("How old are you? ")

#convert input into a an integer
age = int(age)

#react to user's age
if age >= 16:
    print("You can get your driver's!")
elif age == 15:
    print("You can get your learner's!")
else:
    print("You can't drive yet!")

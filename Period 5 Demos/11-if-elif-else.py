age = input("What's your age? ")

age = int(age)

if age == 16:
    print("You can drive!")

elif age < 5:
    print("Not in school yet")

elif age >= 40:
    print("You're over the hill!")

elif age != 12:
    print("You're not 12!")
    
else:
    print("Ok. Nice age.")

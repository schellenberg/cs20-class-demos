name = input("What's your name? ")
age = input("How old are you? ")

age = int(age)

if age >= 16:
    print(f"You can get your drivers, {name} since you are already {age}")

else:
    print(f"You can't drive at age {age}. Please stay off the road, {name}!")
name = input("What's your name? ")
age = input("How old are you? ")
age = float(age)

print("Hello there, " + name)

if age < 16:
    print("You can't drive yet!")
else:
    print("You can get your driver's.")
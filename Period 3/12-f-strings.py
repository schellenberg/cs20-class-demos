name = input("What's your name? ")
age = input("How old are you? ")

age = int(age)

if age >= 16:
    print(f"Hello there, {name}. Since you are {age}, you can drive!")

else:
    print(f"I'm sorry, {name}. Since you are only {age}, you can't drive.")


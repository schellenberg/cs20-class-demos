name = input("What's your name? ")
age = input("How old are you? " )

age = int(age)

if age >= 16:
    print(f"Hi there, {name}. Since you are {age}, you can drive a car.")
else:
    print(f"I'm sorry, {name}. Since you are {age}, you can't drive yet.")
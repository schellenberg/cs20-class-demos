first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
age = input('How old are you? ')

# concatenation
#print("Good afternoon, " + first_name + " " + last_name + ". I hear you are " + age + " years old!")

age = int(age)

# f-string
print(f"Good afternoon, {first_name} {last_name}. I hear you are {age} years old!")

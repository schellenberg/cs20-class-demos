# Input/Output Demo
# Mar 17, 2026
# Dan Schellenberg

#getting info from user
name = input("What's your name? ")
age = input("How old are you? ")

#converting data types
age = int(age)

#outputting to user
if age >= 16:
    print("Hey, " + name + ". You can get your license!")
else:
    print("Sorry " + name + ". You're too young.")

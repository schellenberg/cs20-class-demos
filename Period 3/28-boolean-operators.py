# number = 5
# print(number > 0 and number < 10)

# number = 25
# print(number % 2 == 0 or number % 3 == 0)

#this is a giant screw up! Don't do this!
# number = 7
# if number == 5 or 8:
#     print("Yes")
# else:
#     print("No")
    
#fixed version below
# number = 7
# if number == 5 or number == 8:
#     print("Yes")
# else:
#     print("No")


raining = True
cold = False

print(not raining or not cold and raining)

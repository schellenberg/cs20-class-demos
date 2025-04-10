def square(some_number):
    the_square = some_number * some_number
    return the_square
    
thing_to_square = 5
result = square(thing_to_square)
print(f"{thing_to_square} squared is {result}")

#this is a screw up
#you can't call a local variable outside a function
# print(the_square)

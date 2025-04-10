def square(some_number):
    '''Calculates the square of a number and sends it back.'''
    the_square = some_number * some_number
    return the_square
    
to_square = 10
result = square(to_square)
print(f"{to_square} squared is {result}")

#this is a screw up
#can't access local variables outside functions
#print(the_square)
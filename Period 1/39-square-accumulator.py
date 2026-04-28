def square(some_number):
    '''Returns the square of a number using the accumlator pattern.'''
    the_square = 0
    for counter in range(some_number):
        the_square = the_square + some_number
        
    return the_square

result = square(5)
print(result)
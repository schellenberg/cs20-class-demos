def square(some_number):
    '''Returns the square of a number, using the accumulator pattern.'''
    
    # initialize a variable
    total = 0
    
    # repeat
    for counter in range(some_number):
        # adjust the variable
        total = total + some_number
    
    return total

result = square(6)
print(result)
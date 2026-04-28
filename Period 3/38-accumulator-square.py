def square(number):
    '''Returns the square of number using the accumulator pattern.'''
    the_square = 0
    for counter in range(number):
        the_square = the_square + number
    
    return the_square

answer = square(7)
print(answer)
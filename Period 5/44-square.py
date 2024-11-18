def square(some_number):
    '''Returns the square of some_number.'''
    the_square = some_number * some_number
    return the_square

to_square = input("What number should we square? ")
to_square = int(to_square)
answer = square(to_square)
print(f"The square of {to_square} is {answer}")
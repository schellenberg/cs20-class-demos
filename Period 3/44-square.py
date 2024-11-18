def square(some_number):
    '''Return the square of a number.'''
    the_square = some_number * some_number
    return the_square

to_square = input("What number should I square? ")
to_square = int(to_square)
result = square(to_square)
print(f"The square of {to_square} is {result}.")
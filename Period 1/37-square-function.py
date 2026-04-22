def square(some_number):
    '''Sends back the square of some_number.'''
    the_answer = some_number ** 2
    return the_answer

to_square = input("What number should we square? ")
to_square = int(to_square)
result = square(to_square)
print(f"{to_square} squared is {result}")

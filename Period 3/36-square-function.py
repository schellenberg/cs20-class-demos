def square(some_number):
    '''Return the square of some_number.'''
    answer = some_number * some_number
    return answer

the_number = input("What number should we square? ")
the_number = int(the_number)
result = square(the_number)
print(f"{the_number} squared equals {result}")

def square(number):
    '''Returns the square of a number, using the
       accumlator pattern.'''
    #initialize
    total = 0
    #repeat
    for counter in range(number):
        #change value
        total = total + number
        
    return total

some_number = input("What number should I square? ")
some_number = int(some_number)
result = square(some_number)
print(f'The square of {some_number} is {result}')
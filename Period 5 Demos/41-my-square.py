def my_square(number):
    #initialize
    the_square = 0
    #repeat
    for counter in range(number):      
        #accumulate
        the_square = the_square + number
        
    return the_square

some_number = 3
result = my_square(some_number)
print(f'The square of {some_number} is {result}')
def square(some_number):
    #initialize a counter
    total = 0
    #repeat
    for counter in range(some_number):
        #accumulate
        total = total + some_number
        
    return total


to_square = 7
result = square(to_square)
print(f'The square of {to_square} is {result}')

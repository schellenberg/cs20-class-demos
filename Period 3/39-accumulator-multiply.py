def multiply(first_number, second_number):
    '''Return the product of the numbers.'''
    #initialize accumulator
    product = 0
    #repeat
    for counter in range(first_number):
        #change accumulator
        product = product + second_number
    return product

answer = multiply(7, 5)
print(answer)
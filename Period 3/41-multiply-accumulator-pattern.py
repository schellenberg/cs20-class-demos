def multiply(first_number, second_number):
    '''Returns the two numbers multiplied together.'''
    
    #initialize variable
    product = 0
    #repeat
    for times in range(second_number):
        #change variable
        product = product + first_number
    
    return product

answer = multiply(2, 7)
print(answer)
    
def multiply(first_number, second_number):
    '''Returns the product of first_number and second_number.'''
    
    #initialize variable
    product = 0
    #repeat
    for times in range(second_number):
        #change variable
        product = product + first_number
        
    return product

answer = multiply(2, 7)
print(answer)
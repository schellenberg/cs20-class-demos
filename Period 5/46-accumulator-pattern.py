def multiply(first_number, second_number):
    '''Returns the product of first_number and second_number.'''
    # initialize
    product = 0
    # repeat
    for counter in range(second_number):
        # update variable
        product = product + first_number
    # return answer
    return product

# print(multiply(6, 5))

def square(number):
    '''Return the square of number.'''
    #initialize
    the_square = 0
    #repeat
    for counter in range(number):
        #update variable
        the_square += number
    
    #return answer
    return the_square
    
# print(square(7))
    
    
def sum_to(n):
    '''Returns the sum of the integers between 1 and n.'''
    #initialize
    the_sum = 0
    
    #repeat
    for counter in range(1, n+1):
        #update variable
        the_sum = the_sum + counter
    
    #return answer
    return the_sum
    
print(sum_to(4))
    

    
    
    
    
    
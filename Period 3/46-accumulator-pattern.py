def multiply(first_number, second_number):
    '''Return the two numbers multiplied together.'''
    #initialize
    answer = 0
    #repeat
    for counter in range(second_number):
        #update variable
        answer = answer + first_number
    return answer

# print(multiply(4, 5))

def square(number):
    '''Return the square of a number.'''
    # initialize
    answer = 0
    # repeat
    for counter in range(number):
        # update variable
        answer = answer + number
    return answer

# print(square(5))
        

def sum_to(n):
    '''Returns the sum of the integers from 1 to n'''
    #initialize
    the_sum = 0
    #repeat
    for counter in range(1, n+1):
        #update variable
        the_sum = the_sum + counter
    return the_sum

print(sum_to(4))
    
    
    
    
    
    
    

        
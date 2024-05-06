def sum_to(number):
    '''Returns the sum of all whole numbers from 1 to number.'''
    
    #initialize variable
    the_sum = 0
    #repeat
    for counter in range(1, number + 1):
        #change variable
        the_sum = the_sum + counter
        
    return the_sum

def sum_to_gauss(number):
    '''Returns the sum of whole numbers from 1 to number.'''
    return (number * (number + 1)) / 2

answer = sum_to_gauss(1000000000)
print(answer)
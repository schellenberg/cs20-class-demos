def sum_to(some_number):
    '''Returns the sum of all integers from 1 to some_number.'''
    #initialize variable
    the_sum = 0
    #repeat
    for counter in range(some_number + 1):
        #adjust variable
        the_sum = the_sum + counter
    
    return the_sum

# result = sum_to(1000000000)
# print(result)

def sum_to_gauss(some_number):
    return some_number * (some_number + 1) / 2

result = sum_to_gauss(1000000000)
print(result)

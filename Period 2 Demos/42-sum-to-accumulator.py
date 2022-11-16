def sum_to(number):
    #initialize
    the_sum = 0
    
    #repeat
    for counter in range(number + 1):
        #modify/accumulate
        the_sum = the_sum + counter
        
    return the_sum


print(sum_to(100))
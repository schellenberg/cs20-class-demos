def sum_to(n):
    '''Adds up all the numbers from 1 to n, and returns them'''
    
    #initialize counter
    the_sum = 0
    
    #loop and change the counter
    for number in range(n+1):
        the_sum = the_sum + number
    
    return the_sum
    
def sum_to_optimized(n):
    the_sum = n * (n+1) / 2
    return the_sum

print(sum_to_optimized(1000000000))

def sum_to(n):
    '''Returns the sum of integers from 1 to n.'''

    # initialize variable
    the_sum = 0

    # repeat
    for counter in range(1, n+1):
        # updated variable
        the_sum = the_sum + counter
        
    # variable should be the answer
    return the_sum

def sum_to_faster(n):
    return n*(n+1)/2

print(sum_to_faster(1000000000))
print(sum_to(1000000000))


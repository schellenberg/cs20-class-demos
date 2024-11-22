def sum_to(n):
    '''Return the sum of all integers from 1 to n.'''
    # initialize variable
    answer = 0
    # repeat
    for counter in range(1, n+1):
        # updating variable
        answer = answer + counter
    return answer

def sum_to_faster(n):
    return ((n+1)*n)/2

print(sum_to_faster(1000000000))
print(sum_to(1000000000))


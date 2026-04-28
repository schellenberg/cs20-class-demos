# def sum_to(n):
#     '''Returns the sum of the integers from 1 to n.'''
#     the_sum = 0
#     for counter in range(1, n+1):
#         the_sum = the_sum + counter
#     return the_sum

def sum_to(n):
    '''Use Gauss' method.'''
    return (n/2)*(n+1)

answer = sum_to(10000000000000)
print(answer)
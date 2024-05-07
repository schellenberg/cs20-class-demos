def is_odd(some_number):
    '''Returns True if some_number is odd.
       Returns False if some_number is even.'''
    if some_number % 2 == 1:
        return True
    else:
        return False
    
def is_even(some_number):
    '''Returns True if some_number is even.
       Returns False if some_number is odd.'''
    return not is_odd(some_number)
    
answer = is_even(10)
print(answer)
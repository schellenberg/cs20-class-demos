def is_odd(some_number):
    '''Returns True if the number is odd.
               False if the nunmber is even.'''
    if some_number % 2 == 0:
        return False
    else:
        return True

def is_even(some_number):
    '''Returns True if the number is even.
               False if the nunmber is odd.'''
    return not is_odd(some_number)

print(is_even(7))
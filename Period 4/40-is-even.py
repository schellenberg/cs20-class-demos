def is_even(number):
    '''Return True if number is even, False if odd.'''
    if number % 2 == 0:
        return True
    else:
        return False
    
the_number = input("What's the number? ")
the_number = int(the_number)
if is_even(the_number):
    print("Yup, it's even.")
else:
    print("Nope, it's odd.")
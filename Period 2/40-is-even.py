def is_even(number):
    '''Returns True if the number is even, False if it's odd.'''
    if number % 2 == 0:
        return True
    else:
        return False
    
your_number = input("What number? ")
your_number = int(your_number)

if is_even(your_number):
    print("Yup. It's even")
else:
    print("Nope. It's odd")
    
def multiply(first_number, second_number):
    '''Return the product of the two numbers.'''
    the_product = 0
    for counter in range(first_number):
        the_product = the_product + second_number
    return the_product

answer = multiply(3, 5)
print(answer)
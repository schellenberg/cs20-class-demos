def my_sqrt(n, number_of_guesses):
    '''Return an estimate of the square root using Newton's method.'''
    root = n / 2
    for counter in range(number_of_guesses):
        root = 0.5 * (root + (n/root))
    return root

answer = my_sqrt(16, 6)
print(answer)